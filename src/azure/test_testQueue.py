from unittest import TestCase

from azure.storage.queue import QueueService


class TestTestQueue(TestCase):

    def test_push(self):
        self.client = QueueService(account_name='', account_key='')
        self.client.put_message('testqueue', u"Test message")

