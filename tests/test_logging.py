from bot import MessageLogger
import os

def test_message_logging(tmp_path):
    log_file = tmp_path / "test.log"
    logger = MessageLogger(log_file)
    
    test_message = {
        'message_id': 1,
        'chat': {'id': 1, 'title': "Test Chat"},
        'text': "Токсичное сообщение",
        'from_user': {'id': 1, 'username': "test_user"}
    }
    
    logger.log_deleted_message(test_message)
    
    assert os.path.exists(log_file)
    with open(log_file, 'r') as f:
        content = f.read()
        assert "Токсичное сообщение" in content
        assert "test_user" in content