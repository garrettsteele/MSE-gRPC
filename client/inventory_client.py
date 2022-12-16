
"""The Python implementation of the GRPC Book client."""

from __future__ import print_function

import logging
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'service'))


import grpc
import book_pb2
import book_pb2_grpc


class Inventory_client:

    def run():
        server_location = 'localhost:50051'
        print("Starting gRPC call...")
        with grpc.insecure_channel(server_location) as channel:
            stub = book_pb2_grpc.InventoryServiceStub(channel)
            response = stub.Create_Book(book_pb2.Book(title='The Odyssey', author="Homer", ISBN='9780312866693'))
            print("Success: " + response.success)
            response2 = stub.Get_Book(book_pb2.Book(ISBN='9780312866693'))
            #print(response2)
            print("FROM ISBN, retrieved book: " + response2.title)

    def get_titles(book_isbn):
        server_location = 'localhost:50051'
        #print("Beginning to retrieve books titles based on ISBN...")
        with grpc.insecure_channel(server_location) as channel:
            stub = book_pb2_grpc.InventoryServiceStub(channel)
            response = stub.Get_Book(book_pb2.Book(ISBN = book_isbn))
            #print(response2)
            return response.title

    if __name__ == '__main__':
        logging.basicConfig()
        # get_titles('9780374524524')
        # get_titles('9781452800882')
        # get_titles('9780582541542')
        run()
