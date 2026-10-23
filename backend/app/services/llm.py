from openai import OpenAI

from app.core.config import settings
from app.schemas.chat import ChatMessage

client = OpenAI(api_key=settings.openai_api_key)


def generate_reply(system_prompt: str, history: list[ChatMessage], message: str) -> str:
    msgs = [{"role": "system", "content": system_prompt}]
    msgs += [m.model_dump() for m in history]
    msgs.append({"role": "user", "content": message})

    resp = client.chat.completions.create(
        model=settings.openai_model,
        messages=msgs,
    )

    return resp.choices[0].message.content or ""
