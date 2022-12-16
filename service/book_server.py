
"""The Python implementation of the GRPC book server."""

from concurrent import futures
import logging

import grpc
import book_pb2
import book_pb2_grpc

#  string ISBN = 1;
#  string title = 2;
#  string author = 3;
#  int32 publishing_year = 4;
#  enum Genre {
#     SCIFI = 0;
#     HORROR = 1;
#     ROMANCE = 2;
#     FANTASY = 3;
#  }

book_list = []
inferno = {'ISBN': '9780374524524','title': 'Inferno', 'author': 'Dante',
                    'publishing_year': 1300, 'genre': 'FANTASY'}

cave = {'ISBN': '9781452800882','title': 'Allegory of the Cave', 'author': 'Plato',
                    'publishing_year': 514, 'genre': 'FANTASY'}

frank = {'ISBN': '9780582541542','title': 'Frankenstein', 'author': 'Shelley',
                    'publishing_year': 1818, 'genre': 'HORROR'}

book_list.append(inferno)
book_list.append(cave)
book_list.append(frank)


class InventoryService(book_pb2_grpc.InventoryServiceServicer):

    def Create_Book(self, request, context):
        new_book = {}
        new_book['title'] = request.title
        new_book['author'] = request.author
        new_book['ISBN'] = request.ISBN
        book_list.append(new_book)
        #string_list = ''.join(str(x) for x in book_list)
        return book_pb2.Create_book_reply(success='Created book, %s!' % request.title)#string_list

    def Get_Book(self, request, context):
        #return book_pb2.Book(ISBN='Retrieved book, %s!' % request.ISBN) 
        request_ISBN = request.ISBN
        for book in book_list:
            if request_ISBN in book['ISBN']:
                get_book_response = book['title']
                return book_pb2.Book(ISBN='Retrieved book %s!' % request.ISBN, title=get_book_response)
            # else:
            #     return book_pb2.Book(title='No book found')


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()