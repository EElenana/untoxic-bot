import logging
from unittest.mock import patch
from bot import handle_message
from telegram import Update, Message, User, Chat

def test_logging_on_message_deletion(caplog):
    """Тест логгирования при удалении сообщения"""
    with patch('bot.predict_toxicity', return_value=True):
        mock_update = MagicMock(spec=Update)
        mock_update.message = MagicMock(spec=Message)
        mock_update.message.text = "toxic message"
        mock_update.message.from_user = MagicMock(spec=User)
        mock_update.message.from_user.id = 123
        
        with patch.object(mock_update.message, 'delete'):
            with caplog.at_level(logging.INFO):
                handle_message(mock_update, None)
                
                assert "Удалено сообщение от 123" in caplog.text

def test_logging_on_error(caplog):
    """Тест логгирования ошибок"""
    with patch('bot.predict_toxicity', return_value=True):
        mock_update = MagicMock(spec=Update)
        mock_update.message = MagicMock(spec=Message)
        mock_update.message.delete.side_effect = Exception("Test error")
        
        with caplog.at_level(logging.ERROR):
            handle_message(mock_update, None)
            
            assert "Ошибка удаления: Test error" in caplog.text