import unittest
from unittest.mock import MagicMock, patch
from src.Messenger import Messenger
from assertpy import assert_that


class TestMessenger(unittest.TestCase):
    def setUp(self):
        self.temp = Messenger()

    @patch.object(Messenger, "sendMessage")
    def test_sendmessage_msg_success(self, mock_sendmsg):
        mock_sendmsg.return_value = "Messange has been sent to Michał"
        assert_that(self.temp.sendMessage("Michał", "Hello Michał!")).is_equal_to("Messange has been sent to Michał")

    @patch.object(Messenger, "sendMessage")
    def test_sendmessage_msg_not_string(self, mock_sendmsg):
        mock_sendmsg.side_effect = Exception
        assert_that(self.temp.sendMessage).raises(Exception).when_called_with("Michał", 123)

    @patch.object(Messenger, "sendMessage")
    def test_sendmessage_client_not_string(self, mock_sendmsg):
        mock_sendmsg.side_effect = Exception
        assert_that(self.temp.sendMessage).raises(Exception).when_called_with(123, "Hello!")

    @patch.object(Messenger, "receiveMessage")
    def test_receivemessage_msg_success(self, mock_receivemsg):
        mock_receivemsg.return_value = "Received message from Michał: Hello there!"
        assert_that(self.temp.receiveMessage("Michał")).is_equal_to("Received message from Michał: Hello there!")

    @patch.object(Messenger, "receiveMessage")
    def test_receivemessage_client_not_string(self, mock_sendmsg):
        mock_sendmsg.side_effect = Exception
        assert_that(self.temp.receiveMessage).raises(Exception).when_called_with(123)

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    unittest.main()
