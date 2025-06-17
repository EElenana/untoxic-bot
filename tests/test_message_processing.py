from unittest.mock import MagicMock, patch
from bot import handle_message


def test_handle_message_toxic():
    mock_update = MagicMock()
    mock_message = MagicMock()
    mock_update.message = mock_message
    
    with patch('bot.predict_toxicity', return_value=True):
        handle_message(mock_update, None)
        mock_message.delete.assert_called_once()


def test_handle_message_clean():
    mock_update = MagicMock()
    mock_message = MagicMock()
    mock_update.message = mock_message
    
    with patch('bot.predict_toxicity', return_value=False):
        handle_message(mock_update, None)
        mock_message.delete.assert_not_called()