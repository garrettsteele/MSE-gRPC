
"""The Python implementation of the GRPC Book client."""

from __future__ import print_function

import logging
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'service'))


import grpc
import book_pb2
import book_pb2_grpc
from get_book_titles import Get_book_titles as titles
from inventory_client import Inventory_client as client
from unittest.mock import patch, MagicMock, Mock
import unittest


class TestInventoryClient(unittest.TestCase):

    def log_calls(self, args):
        if args == '9780374524524':
            return "Inferno"
        elif args == '9780582541542':
            return "Frankenstein"
        elif args == '9781452800882':
            return "Allegory of the Cave"
        else:
            return "invalid"

    def test_book_titles_Mock(self): #mock_get_titles
        mocked_client = client()
        mocked_client.get_titles = MagicMock()
        mocked_client.get_titles.return_value = 'adf'
        mocked_client.get_titles.side_effect = self.log_calls
        ISBN_list = ['9780374524524', '9780582541542', '9781452800882']
        returned_list = titles.get_book_titles(ISBN_list=ISBN_list, client=mocked_client)

        expected_list = ['Inferno','Frankenstein', 'Allegory of the Cave']
        self.assertListEqual(returned_list,expected_list)

    def test_book_titles_live(self):
        ISBN_list = ['9780374524524', '9780582541542', '9781452800882']
        returned_list = titles.get_book_titles(ISBN_list=ISBN_list, client=client)
        expected_list = ['Inferno', 'Frankenstein', 'Allegory of the Cave']
        self.assertListEqual(returned_list,expected_list)


if __name__ == '__main__':
    unittest.main()