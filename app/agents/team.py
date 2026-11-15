
"""MediBot multi-agent team.

Three Agno agents collaborate through a Team in TeamMode.coordinate:
1. Query Analyzer - classifies the health topic and extracts facts.
2. Research Agent - uses healthcare library excerpts for grounded information.
3. Answer Reviewer - checks safety and produces the final answer.
"""

from typing import Any, Dict, Optional

from app import config
from app.agents.tools import (
    clear_consulted_sources,
    get_last_consulted_sources,
    search_library,
)

AGENT_NAMES = ["Query Analyzer", "Research Agent", "Answer Reviewer"]


def create_model_instance(api_key: Optional[str] = None, model_id: Optional[str] = None):
    """Create the LLM object for the active provider."""
    if config.MODEL_PROVIDER == "google":
        from agno.models.google import Gemini

        return Gemini(
            id=model_id or config.GEMINI_MODEL,
            api_key=api_key if api_key is not None else config.GEMINI_API_KEY,
        )

    from agno.models.groq import Groq

    return Groq(
        id=model_id or config.GROQ_MODEL,
        api_key=api_key if api_key is not None else config.GROQ_API_KEY,
    )


def build_team(api_key: Optional[str] = None, model_id: Optional[str] = None):
    """Build the three agents and coordinate them with an Agno Team."""
    from agno.agent import Agent
    from agno.team import Team, TeamMode

    model = create_model_instance(api_key=api_key, model_id=model_id)

    analyzer = Agent(
        name="Query Analyzer",
        role="Classify the health question and extract important facts.",
        model=model,
        telemetry=False,
        description="A careful health-information analyst.",
        instructions=[
            "Identify the health topic and classify the user's question.",
            "Extract symptoms, duration, age group and medicines if provided.",
            "Identify important missing information.",
            "Flag possible emergency warning signs.",
            "Pass a short analysis to the Research Agent.",
        ],
    )

    researcher = Agent(
        name="Research Agent",
        role="Research the healthcare library and provide grounded information.",
        model=model,
        tools=[search_library],
        telemetry=False,
        description="A medical information researcher.",
        instructions=[
            "Use the healthcare library excerpts provided in the task context.",
            "Do not call search_library again because the library has already been searched.",
            "Use only information supported by the provided library excerpts.",
            "Do not invent medical facts, statistics or recommendations.",
            "Mention the library documents used when that information is available.",
            "Pass the findings to the Answer Reviewer.",
        ],
    )

    reviewer = Agent(
        name="Answer Reviewer",
        role="Review medical information and produce a safe final answer.",
        model=model,
        telemetry=False,
        description="A cautious clinical-safety reviewer.",
        instructions=[
            "Check the findings against the provided research information.",
            "Remove unsupported or speculative claims.",
            "Never diagnose or prescribe medicines.",
            "Do not provide medicine doses unless explicitly supported by the library.",
            "Include when to consult a doctor and emergency warning signs.",
            "Use these headings:",
            "Topic & Summary",
            "Key Facts & Guidelines",
            "Self-care & Practical Steps",
            "When to See a Doctor",
            "Reviewer Audit Note",
            "Write in simple English for a general reader.",
        ],
    )

    return Team(
        name="MediBot Healthcare Team",
        members=[analyzer, researcher, reviewer],
        model=model,
        mode=TeamMode.coordinate,
        telemetry=False,
        instructions=[
            "Coordinate the three agents to answer the user's question.",
            "First, Query Analyzer identifies the health topic and important facts.",
            "Second, Research Agent uses the supplied healthcare library excerpts.",
            "Third, Answer Reviewer checks safety and writes the final answer.",
            "Do not perform another library search because excerpts are already supplied.",
            "Return only the final reviewed answer.",
        ],
    )


def run_workflow(question: str, team=None) -> Dict[str, Any]:
    """Run the healthcare workflow and return the answer and consulted sources."""

    clear_consulted_sources()

    # Search the healthcare library once before starting the team.
    library_excerpts = search_library(question)

    prompt = (
        "You are MediBot, a healthcare assistant consisting of three agents: "
        "Query Analyzer, Research Agent and Answer Reviewer.\n\n"
        f"USER QUESTION:\n{question}\n\n"
        f"HEALTHCARE LIBRARY EXCERPTS:\n{library_excerpts}\n\n"
        "Follow the three-agent workflow. Use the provided library excerpts "
        "as the research source. Do not diagnose or prescribe medicines. "
        "Do not invent unsupported medical facts. Explain practical self-care, "
        "when to consult a doctor and emergency warning signs.\n\n"
        "Write the final answer using these headings:\n"
        "1. Topic & Summary\n"
        "2. Key Facts & Guidelines\n"
        "3. Self-care & Practical Steps\n"
        "4. When to See a Doctor\n"
        "5. Reviewer Audit Note\n\n"
        "Use simple English."
    )

    active_team = team if team is not None else build_team()

    output = active_team.run(prompt)

    if hasattr(output, "get_content_as_string"):
        answer = output.get_content_as_string()
    elif getattr(output, "content", None):
        answer = str(output.content)
    else:
        answer = str(output)

    return {
        "answer": answer.strip(),
        "sources": get_last_consulted_sources(),
    }
