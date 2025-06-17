from bot import MessageProcessor
from telegram import Message, Chat, User

@pytest.fixture
def processor():
    return MessageProcessor()

def test_process_toxic_message(processor, mocker):
    """Тест обработки токсичного сообщения"""
    mock_delete = mocker.patch('bot.Message.delete')
    
    chat = Chat(id=1, type='group')
    user = User(id=1, first_name="Test")
    message = Message(
        message_id=1,
        date=None,
        chat=chat,
        from_user=user,
        text="Ты тупой!"
    )
    
    mocker.patch('model.ToxicityClassifier.predict', return_value=(1, 0.9))
    
    processor.process_message(message)
    
    mock_delete.assert_called_once()

def test_process_clean_message(processor, mocker):
    """Тест обработки нормального сообщения"""
    mock_delete = mocker.patch('bot.Message.delete')
    
    message = Message(
        message_id=2,
        date=None,
        chat=Chat(id=1, type='group'),
        text="Привет, как дела?"
    )
    
    mocker.patch('model.ToxicityClassifier.predict', return_value=(0, 0.1))
    
    processor.process_message(message)
    
    mock_delete.assert_not_called()