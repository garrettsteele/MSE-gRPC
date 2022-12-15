
"""The Python implementation of the GRPC Book client."""

from __future__ import print_function

import logging

import grpc
import book_pb2
import book_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Starting gRPC call...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.InventoryServiceStub(channel)
        response = stub.Create_Book(book_pb2.Book(title='The Odyssey', author="Homer", ISBN='9780312866693'))
        print("Success: " + response.success)
        response2 = stub.Get_Book(book_pb2.Book(ISBN='9780312866693'))
        #print(response2)
        print("FROM ISBN, retrieved book: " + response2.title)


if __name__ == '__main__':
    logging.basicConfig()
    run()
