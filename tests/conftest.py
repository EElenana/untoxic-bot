import pytest
from unittest.mock import MagicMock
from telegram import Update, Message, User, Chat

@pytest.fixture
def mock_update():
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.text = "test message"
    update.message.from_user = MagicMock(spec=User)
    update.message.from_user.id = 123
    update.message.chat = MagicMock(spec=Chat)
    return update