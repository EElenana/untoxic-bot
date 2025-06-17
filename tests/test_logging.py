import logging
from unittest.mock import MagicMock, patch
from bot import handle_message


def test_logging_on_message_deletion(caplog):
    mock_update = MagicMock()
    mock_message = MagicMock()
    mock_message.from_user.id = 123
    mock_update.message = mock_message
    
    with patch('bot.predict_toxicity', return_value=True):
        with caplog.at_level(logging.INFO):
            handle_message(mock_update, None)
            assert "Удалено сообщение от 123" in caplog.text


def test_logging_on_error(caplog):
    mock_update = MagicMock()
    mock_message = MagicMock()
    mock_message.delete.side_effect = Exception("Test error")
    mock_update.message = mock_message
    
    with patch('bot.predict_toxicity', return_value=True):
        with caplog.at_level(logging.ERROR):
            handle_message(mock_update, None)
            assert "Ошибка удаления: Test error" in caplog.text"