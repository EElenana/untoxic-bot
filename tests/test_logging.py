import logging
from unittest.mock import MagicMock, patch
from bot import handle_message
import pytest

def test_logging_on_message_deletion(caplog):
    """Тест логгирования при удалении сообщения"""
    # Создаем mock-объекты для Update и Message
    mock_update = MagicMock()
    mock_message = MagicMock()
    mock_message.from_user.id = 123
    mock_update.message = mock_message
    
    with patch('bot.predict_toxicity', return_value=True):
        with caplog.at_level(logging.INFO):
            handle_message(mock_update, None)
            
            # Проверяем, что сообщение залогировано
            assert "Удалено сообщение от 123" in caplog.text

def test_logging_on_error(caplog):
    """Тест логгирования ошибок"""
    # Создаем mock-объекты
    mock_update = MagicMock()
    mock_message = MagicMock()
    mock_update.message = mock_message
    mock_message.delete.side_effect = Exception("Test error")
    
    with patch('bot.predict_toxicity', return_value=True):
        with caplog.at_level(logging.ERROR):
            handle_message(mock_update, None)
            
            # Проверяем, что ошибка залогирована
            assert "Ошибка удаления: Test error" in caplog.text