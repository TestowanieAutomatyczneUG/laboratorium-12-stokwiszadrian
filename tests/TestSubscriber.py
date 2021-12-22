import unittest
from unittest.mock import Mock, patch
from src.Subscriber import Subscriber
from assertpy import assert_that

class TestSubscriber(unittest.TestCase):
    @patch(Subscriber, 'getClient', Mock(return_value=True))
    def test_addClient(self, mock):
        assert_that(mock.getClients()).is_true()
