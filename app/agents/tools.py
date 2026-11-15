"""Tools for the MediBot agents.

`search_library` lets the Research Agent look up grounding documents and records
which documents were consulted so they can be shown to the user as sources.
"""

from typing import List, Set
from app.data.sample_documents import SAMPLE_DOCUMENTS

_last_consulted_sources: Set[str] = set()


def get_last_consulted_sources() -> List[str]:
    """Titles of documents consulted during the most recent research session."""
    return sorted(_last_consulted_sources)


def clear_consulted_sources() -> None:
    """Reset the source tracker before starting a new question."""
    _last_consulted_sources.clear()


def search_library(query: str) -> str:
    """Search the healthcare knowledge library for relevant guidance.

    Args:
        query: Keywords, topic or question to search for (e.g. "fever sore throat").

    Returns:
        Relevant excerpts with document titles, or the list of available topics if nothing matched.
    """
    if not query or not query.strip():
        return "No query provided. Please specify health topics, symptoms or keywords."

    tokens = [w.lower().strip("?,.;:\"'()") for w in query.split() if len(w) > 2]
    matches = []

    for doc in SAMPLE_DOCUMENTS:
        keywords = [k.lower() for k in doc["keywords"]]
        title = doc["title"].lower()
        category = doc["category"].lower()
        content = doc["content"].lower()
        score = 0
        for t in tokens:
            if t in keywords:
                score += 3
            if t in title:
                score += 4
            if t in category:
                score += 2
            if t in content:
                score += 1
        if score > 0:
            matches.append((score, doc))

    if not matches:
        titles = ", ".join(f"'{d['title']}'" for d in SAMPLE_DOCUMENTS)
        return f"No direct matches found for '{query}'. Topics available in the library: {titles}."

    matches.sort(key=lambda m: m[0], reverse=True)
    results: List[str] = []
    for _, doc in matches[:2]:
        _last_consulted_sources.add(doc["title"])
        results.append(f"[{doc['title']}]\nSummary: {doc['summary']}\nKey points:\n{doc['content']}\n")
    return "\n".join(results)
