import pytest
from unittest.mock import MagicMock, patch
from bot import handle_message
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

def test_handle_message_toxic(mock_update):
    with patch('bot.predict_toxicity', return_value=True):
        with patch.object(mock_update.message, 'delete') as mock_delete:
            handle_message(mock_update, None)
            mock_delete.assert_called_once()

def test_handle_message_clean(mock_update):
    with patch('bot.predict_toxicity', return_value=False):
        with patch.object(mock_update.message, 'delete') as mock_delete:
            handle_message(mock_update, None)
            mock_delete.assert_not_called()