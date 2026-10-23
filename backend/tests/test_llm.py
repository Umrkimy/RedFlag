from types import SimpleNamespace

from app.schemas.chat import ChatMessage
from app.services import llm


class FakeCompletions:
    def __init__(self, content):
        self.content = content
        self.sent = None

    def create(self, model, messages):
        self.sent = messages
        message = SimpleNamespace(content=self.content)
        return SimpleNamespace(choices=[SimpleNamespace(message=message)])


def use_fake(monkeypatch, content):
    fake = FakeCompletions(content)
    fake_client = SimpleNamespace(chat=SimpleNamespace(completions=fake))
    monkeypatch.setattr(llm, "client", fake_client)
    return fake


def test_messages_order(monkeypatch):
    fake = use_fake(monkeypatch, "hi")
    history = [ChatMessage(role="user", content="a")]

    result = llm.generate_reply("SYS", history, "b")

    assert [m["role"] for m in fake.sent] == ["system", "user", "user"]
    assert fake.sent[0]["content"] == "SYS"
    assert fake.sent[-1]["content"] == "b"
    assert result == "hi"


def test_none_content_returns_empty(monkeypatch):
    use_fake(monkeypatch, None)

    assert llm.generate_reply("SYS", [], "b") == ""
