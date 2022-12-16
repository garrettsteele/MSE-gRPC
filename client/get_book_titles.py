
"""The Python implementation of the GRPC Book client."""

from __future__ import print_function

import logging
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'service'))

import grpc
import book_pb2
import book_pb2_grpc
from inventory_client import Inventory_client as client


class Get_book_titles:

    def get_book_titles(ISBN_list, client):
        return_list = []
        for isbn in ISBN_list:
            return_list.append(client.get_titles(isbn)) 
        return return_list



    if __name__ == '__main__':
        logging.basicConfig()
        ISBN_list = ['9780374524524', '9780582541542', '9781452800882']

        title_list = get_book_titles(ISBN_list, client)
        for title in title_list:
            print(title)
