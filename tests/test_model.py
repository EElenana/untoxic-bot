import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model import predict_toxicity


def test_predict_returns_bool():
    result = predict_toxicity("Ты молодец, продолжай в том же духе!")
    assert isinstance(result, bool)


def test_predict_toxic_text():
    result = predict_toxicity("Ты жалкий идиот, у тебя ничего не получится.")
    assert result is True


def test_predict_neutral_text():
    result = predict_toxicity("Доброе утро! Сегодня хорошая погода.")
    assert result is False


def test_predict_empty_string():
    result = predict_toxicity("")
    assert result is False
