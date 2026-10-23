from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm import generate_reply
from app.services.prompt import build_system_prompt
from app.services.truth_sheet import load_truth_sheet

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        sheet = load_truth_sheet(req.case_id, req.character_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Character not found") from None

    system_prompt = build_system_prompt(sheet, req.evidence_shown)
    reply = generate_reply(system_prompt, req.history, req.message)

    return ChatResponse(reply=reply)
