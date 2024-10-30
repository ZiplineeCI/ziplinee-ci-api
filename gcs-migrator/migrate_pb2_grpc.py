# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import migrate_pb2 as migrate__pb2


class ServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Migrate = channel.stream_unary(
                '/migrationpb.Service/Migrate',
                request_serializer=migrate__pb2.Request.SerializeToString,
                response_deserializer=migrate__pb2.Response.FromString,
                )


class ServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Migrate(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Migrate': grpc.stream_unary_rpc_method_handler(
                    servicer.Migrate,
                    request_deserializer=migrate__pb2.Request.FromString,
                    response_serializer=migrate__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'migrationpb.Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Migrate(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/migrationpb.Service/Migrate',
            migrate__pb2.Request.SerializeToString,
            migrate__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class LogCheckStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Check = channel.stream_unary(
                '/migrationpb.LogCheck/Check',
                request_serializer=migrate__pb2.LogObject.SerializeToString,
                response_deserializer=migrate__pb2.LogCheckResponse.FromString,
                )


class LogCheckServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Check(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogCheckServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Check': grpc.stream_unary_rpc_method_handler(
                    servicer.Check,
                    request_deserializer=migrate__pb2.LogObject.FromString,
                    response_serializer=migrate__pb2.LogCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'migrationpb.LogCheck', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LogCheck(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Check(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/migrationpb.LogCheck/Check',
            migrate__pb2.LogObject.SerializeToString,
            migrate__pb2.LogCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class HealthStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Check = channel.unary_unary(
                '/migrationpb.Health/Check',
                request_serializer=migrate__pb2.HealthCheckRequest.SerializeToString,
                response_deserializer=migrate__pb2.HealthCheckResponse.FromString,
                )


class HealthServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HealthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Check': grpc.unary_unary_rpc_method_handler(
                    servicer.Check,
                    request_deserializer=migrate__pb2.HealthCheckRequest.FromString,
                    response_serializer=migrate__pb2.HealthCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'migrationpb.Health', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Health(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Check(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/migrationpb.Health/Check',
            migrate__pb2.HealthCheckRequest.SerializeToString,
            migrate__pb2.HealthCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
