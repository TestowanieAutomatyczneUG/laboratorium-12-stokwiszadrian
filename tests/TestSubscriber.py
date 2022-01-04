import unittest
from unittest.mock import MagicMock, patch
from src.Subscriber import Subscriber
from assertpy import assert_that


class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.temp = Subscriber()

    @patch.object(Subscriber, 'addClient')
    def test_addClient_adding(self, mock_add):
        mock_add.return_value = "Michał"
        assert_that(self.temp.addClient("Michał")).is_equal_to("Michał")

    @patch.object(Subscriber, 'addClient')
    def test_addClient_client_integer(self, mock_add):
        mock_add.side_effect = Exception
        assert_that(self.temp.addClient).raises(Exception).when_called_with(2)

    @patch.object(Subscriber, 'addClient')
    def test_addClient_client_dict(self, mock_add):
        mock_add.side_effect = Exception
        assert_that(self.temp.addClient).raises(Exception).when_called_with({"name": "Michał"})

    @patch.object(Subscriber, 'addClient')
    def test_addClient_already_exists(self, mock_add):
        mock_add.side_effect = Exception
        self.temp.clients = ["Michał"]
        assert_that(self.temp.addClient).raises(Exception).when_called_with("Michał")

    @patch.object(Subscriber, 'deleteClient')
    def test_deleteClient_deleting(self, mock_delete):
        self.temp.clients = ["Michał"]
        mock_delete.return_value = "Michał"
        assert_that(self.temp.deleteClient("Michał")).is_equal_to("Michał")

    @patch.object(Subscriber, 'deleteClient')
    def test_deleteClient_client_integer(self, mock_delete):
        mock_delete.side_effect = Exception
        assert_that(self.temp.deleteClient).raises(Exception).when_called_with(2)

    @patch.object(Subscriber, 'deleteClient')
    def test_deleteClient_client_dict(self, mock_delete):
        mock_delete.side_effect = Exception
        assert_that(self.temp.deleteClient).raises(Exception).when_called_with({"name": "Michał"})

    @patch.object(Subscriber, 'deleteClient')
    def test_deleteClient_empty(self, mock_delete):
        mock_delete.side_effect = Exception
        assert_that(self.temp.deleteClient).raises(Exception).when_called_with("Michał")

    @patch.object(Subscriber, 'messageClient')
    def test_messageClient_success(self, mock_msg):
        self.temp.clients = ["Michał"]
        mock_msg.return_value = {"client": "Michał", "message": "Hello Michał!"}
        assert_that(self.temp.messageClient("Michał", "Hello Michał!")).is_equal_to({"client": "Michał", "message": "Hello Michał!"}, include=["client", "message"])

    @patch.object(Subscriber, 'messageClient')
    def test_messageClient_client_integer(self, mock_msg):
        mock_msg.side_effect = Exception
        self.temp.clients = ["Michał"]
        assert_that(self.temp.messageClient).raises(Exception).when_called_with(2, "Hello 2!")

    @patch.object(Subscriber, 'messageClient')
    def test_messageClient_message_integer(self, mock_msg):
        mock_msg.side_effect = Exception
        self.temp.clients = ["Michał"]
        assert_that(self.temp.messageClient).raises(Exception).when_called_with("Michał", 2)

    @patch.object(Subscriber, 'messageClient')
    def test_messageClient_client_dict(self, mock_msg):
        mock_msg.side_effect = Exception
        self.temp.clients = ["Michał"]
        assert_that(self.temp.messageClient).raises(Exception).when_called_with({"name": "Michał"}, "Hello Michał!")

    @patch.object(Subscriber, 'messageClient')
    def test_messageClient_message_dict(self, mock_msg):
        mock_msg.side_effect = Exception
        self.temp.clients = ["Michał"]
        assert_that(self.temp.messageClient).raises(Exception).when_called_with("Michał", {"msg": "Hello Michał!"})

    @patch.object(Subscriber, 'messageClient')
    def test_messageClient_client_notfound(self, mock_msg):
        mock_msg.side_effect = Exception
        assert_that(self.temp.messageClient).raises(Exception).when_called_with("Michał", "Hello Michał!")

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    unittest.main()
