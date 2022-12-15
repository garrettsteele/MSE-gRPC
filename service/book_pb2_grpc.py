# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import book_pb2 as book__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create_Book = channel.unary_unary(
                '/book.InventoryService/Create_Book',
                request_serializer=book__pb2.Book.SerializeToString,
                response_deserializer=book__pb2.Create_book_reply.FromString,
                )
        self.Get_Book = channel.unary_unary(
                '/book.InventoryService/Get_Book',
                request_serializer=book__pb2.Book.SerializeToString,
                response_deserializer=book__pb2.Book.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create_Book(self, request, context):
        """A simple RPC.

        Obtains the MessageResponse at a given position.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get_Book(self, request, context):
        """
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create_Book': grpc.unary_unary_rpc_method_handler(
                    servicer.Create_Book,
                    request_deserializer=book__pb2.Book.FromString,
                    response_serializer=book__pb2.Create_book_reply.SerializeToString,
            ),
            'Get_Book': grpc.unary_unary_rpc_method_handler(
                    servicer.Get_Book,
                    request_deserializer=book__pb2.Book.FromString,
                    response_serializer=book__pb2.Book.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'book.InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create_Book(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book.InventoryService/Create_Book',
            book__pb2.Book.SerializeToString,
            book__pb2.Create_book_reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get_Book(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book.InventoryService/Get_Book',
            book__pb2.Book.SerializeToString,
            book__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)