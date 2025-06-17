import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_update():
    update = MagicMock()
    message = MagicMock()
    message.from_user.id = 123
    update.message = message
    return update
