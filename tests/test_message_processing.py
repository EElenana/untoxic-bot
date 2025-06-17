from unittest.mock import MagicMock, patch
from bot import handle_message
import pytest

def test_handle_message_toxic():
    """Тест обработки токсичного сообщения"""
    # Создаем mock-объекты
    mock_update = MagicMock()
    mock_message = MagicMock()
    mock_update.message = mock_message
    
    with patch('bot.predict_toxicity', return_value=True):
        handle_message(mock_update, None)
        mock_message.delete.assert_called_once()

def test_handle_message_clean():
    """Тест обработки нормального сообщения"""
    mock_update = MagicMock()
    mock_message = MagicMock()
    mock_update.message = mock_message
    
    with patch('bot.predict_toxicity', return_value=False):
        handle_message(mock_update, None)
        mock_message.delete.assert_not_called()