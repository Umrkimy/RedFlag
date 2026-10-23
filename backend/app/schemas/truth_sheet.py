from pydantic import BaseModel


class HiddenFact(BaseModel):
    id: str
    fact: str
    unlock_by: str


class Lie(BaseModel):
    claim: str
    truth: str


class TruthSheet(BaseModel):
    id: str
    name: str
    persona: str
    knows: list[str]
    hides: list[HiddenFact]
    lies: list[Lie]
