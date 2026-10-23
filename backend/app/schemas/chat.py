from typing import Literal

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(max_length=1000)


class ChatRequest(BaseModel):
    case_id: str = Field(pattern=r"^[a-zA-Z0-9_-]+$")
    character_id: str = Field(pattern=r"^[a-zA-Z0-9_-]+$")
    message: str = Field(min_length=1, max_length=500)
    history: list[ChatMessage] = Field(default_factory=list, max_length=20)
    evidence_shown: list[str] = Field(default_factory=list, max_length=50)


class ChatResponse(BaseModel):
    reply: str
