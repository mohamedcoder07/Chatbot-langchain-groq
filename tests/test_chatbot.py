import pytest


from chatbot import ask_llm

class FakeResponse:
    content = "Bonjour !"


class FakeLLM:
    def __init__(self):
        self.question = None

    def invoke(self, question):
        self.question = question
        return FakeResponse()



def test_ask_llm(monkeypatch):
    monkeypatch.setattr("chatbot.llm", FakeLLM())

    result = ask_llm("Bonjour")

    assert result == "Bonjour !"


def test_ask_llm_question(monkeypatch):
    fake_llm = FakeLLM()

    monkeypatch.setattr("chatbot.llm", fake_llm)

    ask_llm("Quelle est la capitale du Maroc ?")

    assert fake_llm.question == "Quelle est la capitale du Maroc ?"