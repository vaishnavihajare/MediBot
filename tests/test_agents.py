import pytest
from app.agents.team import AGENT_NAMES
from app.agents.tools import clear_consulted_sources, get_last_consulted_sources, search_library


def test_three_agents_registered():
    assert AGENT_NAMES == ["Query Analyzer", "Research Agent", "Answer Reviewer"]


def test_search_finds_fever_document():
    clear_consulted_sources()
    result = search_library("fever and sore throat")
    assert "Fever" in result
    assert any("Fever" in s for s in get_last_consulted_sources())


def test_search_finds_blood_pressure_document():
    clear_consulted_sources()
    assert "Blood Pressure" in search_library("high blood pressure salt")


def test_search_empty_query():
    assert "No query" in search_library("   ")


def test_team_has_three_members_and_tool():
    pytest.importorskip("agno")
    from app.agents.team import build_team

    team = build_team(api_key="dummy-key-for-test")
    assert len(team.members) == 3
    researcher = [m for m in team.members if m.name == "Research Agent"][0]
    assert researcher.tools
