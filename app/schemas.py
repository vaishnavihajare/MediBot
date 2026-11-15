"""Pydantic schemas for MediBot API requests and responses."""

from typing import List, Optional
from pydantic import BaseModel, Field, field_validator


class QuestionRequest(BaseModel):
    """Schema for incoming user health questions."""
    question: str = Field(
        ...,
        min_length=5,
        max_length=2000,
        description="The health question to analyze.",
        examples=["I have had a fever for two days. When should I see a doctor?"]
    )

    @field_validator("question")
    @classmethod
    def validate_question_content(cls, value: str) -> str:
        trimmed = value.strip()
        if len(trimmed) < 5:
            raise ValueError("Question must contain at least 5 non-whitespace characters.")
        return trimmed


class BotResponse(BaseModel):
    """Schema for multi-agent healthcare response."""
    status: str = Field(default="success", description="Status of the analysis.")
    question: str = Field(..., description="The original question submitted.")
    answer: str = Field(..., description="Synthesized, reviewed answer.")
    category: Optional[str] = Field(default=None, description="Identified health topic.")
    sources: List[str] = Field(default_factory=list, description="Library sources consulted.")
    disclaimer: str = Field(..., description="Mandatory medical disclaimer.")


class HealthResponse(BaseModel):
    """Schema for application health check endpoint."""
    status: str = Field(default="healthy")
    app_name: str
    groq_configured: bool
    model: str
    agents: List[str]
