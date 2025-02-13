# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import lms_pb2 as lms__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in lms_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LMSStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/LMS/Login',
                request_serializer=lms__pb2.LoginRequest.SerializeToString,
                response_deserializer=lms__pb2.LoginResponse.FromString,
                _registered_method=True)
        self.Logout = channel.unary_unary(
                '/LMS/Logout',
                request_serializer=lms__pb2.LogoutRequest.SerializeToString,
                response_deserializer=lms__pb2.StatusResponse.FromString,
                _registered_method=True)
        self.PostQuery = channel.unary_unary(
                '/LMS/PostQuery',
                request_serializer=lms__pb2.PostQueryRequest.SerializeToString,
                response_deserializer=lms__pb2.PostQueryReply.FromString,
                _registered_method=True)
        self.GetQueries = channel.unary_unary(
                '/LMS/GetQueries',
                request_serializer=lms__pb2.GetQueriesRequest.SerializeToString,
                response_deserializer=lms__pb2.GetQueriesReply.FromString,
                _registered_method=True)
        self.RespondToQuery = channel.unary_unary(
                '/LMS/RespondToQuery',
                request_serializer=lms__pb2.RespondToQueryRequest.SerializeToString,
                response_deserializer=lms__pb2.RespondToQueryReply.FromString,
                _registered_method=True)
        self.PostCourseMaterial = channel.unary_unary(
                '/LMS/PostCourseMaterial',
                request_serializer=lms__pb2.PostMaterialRequest.SerializeToString,
                response_deserializer=lms__pb2.PostMaterialResponse.FromString,
                _registered_method=True)
        self.GetCourseMaterials = channel.unary_unary(
                '/LMS/GetCourseMaterials',
                request_serializer=lms__pb2.GetCourseMaterialsRequest.SerializeToString,
                response_deserializer=lms__pb2.GetCourseMaterialsReply.FromString,
                _registered_method=True)
        self.PostAssignment = channel.unary_unary(
                '/LMS/PostAssignment',
                request_serializer=lms__pb2.PostAssignmentRequest.SerializeToString,
                response_deserializer=lms__pb2.PostAssignmentReply.FromString,
                _registered_method=True)
        self.GetAssignments = channel.unary_unary(
                '/LMS/GetAssignments',
                request_serializer=lms__pb2.GetAssignmentsRequest.SerializeToString,
                response_deserializer=lms__pb2.GetAssignmentsReply.FromString,
                _registered_method=True)
        self.SubmitAssignment = channel.unary_unary(
                '/LMS/SubmitAssignment',
                request_serializer=lms__pb2.SubmitAssignmentRequest.SerializeToString,
                response_deserializer=lms__pb2.SubmitAssignmentReply.FromString,
                _registered_method=True)
        self.GetSubmissions = channel.unary_unary(
                '/LMS/GetSubmissions',
                request_serializer=lms__pb2.GetSubmissionsRequest.SerializeToString,
                response_deserializer=lms__pb2.GetSubmissionsReply.FromString,
                _registered_method=True)
        self.GradeSubmission = channel.unary_unary(
                '/LMS/GradeSubmission',
                request_serializer=lms__pb2.GradeSubmissionRequest.SerializeToString,
                response_deserializer=lms__pb2.GradeSubmissionReply.FromString,
                _registered_method=True)
        self.ViewGrades = channel.unary_unary(
                '/LMS/ViewGrades',
                request_serializer=lms__pb2.ViewGradesRequest.SerializeToString,
                response_deserializer=lms__pb2.ViewGradesReply.FromString,
                _registered_method=True)
        self.CheckLeader = channel.unary_unary(
                '/LMS/CheckLeader',
                request_serializer=lms__pb2.LeaderRequest.SerializeToString,
                response_deserializer=lms__pb2.LeaderResponse.FromString,
                _registered_method=True)
        self.RequestVote = channel.unary_unary(
                '/LMS/RequestVote',
                request_serializer=lms__pb2.RequestVoteRequest.SerializeToString,
                response_deserializer=lms__pb2.RequestVoteResponse.FromString,
                _registered_method=True)
        self.AppendEntries = channel.unary_unary(
                '/LMS/AppendEntries',
                request_serializer=lms__pb2.AppendEntriesRequest.SerializeToString,
                response_deserializer=lms__pb2.AppendEntriesResponse.FromString,
                _registered_method=True)
        self.AnnounceLeader = channel.unary_unary(
                '/LMS/AnnounceLeader',
                request_serializer=lms__pb2.LeaderAnnouncement.SerializeToString,
                response_deserializer=lms__pb2.Empty.FromString,
                _registered_method=True)


class LMSServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login(self, request, context):
        """Login and logout are shared between students and instructors
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetQueries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondToQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostCourseMaterial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCourseMaterials(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostAssignment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAssignments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitAssignment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSubmissions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GradeSubmission(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ViewGrades(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckLeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestVote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppendEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AnnounceLeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LMSServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=lms__pb2.LoginRequest.FromString,
                    response_serializer=lms__pb2.LoginResponse.SerializeToString,
            ),
            'Logout': grpc.unary_unary_rpc_method_handler(
                    servicer.Logout,
                    request_deserializer=lms__pb2.LogoutRequest.FromString,
                    response_serializer=lms__pb2.StatusResponse.SerializeToString,
            ),
            'PostQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.PostQuery,
                    request_deserializer=lms__pb2.PostQueryRequest.FromString,
                    response_serializer=lms__pb2.PostQueryReply.SerializeToString,
            ),
            'GetQueries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetQueries,
                    request_deserializer=lms__pb2.GetQueriesRequest.FromString,
                    response_serializer=lms__pb2.GetQueriesReply.SerializeToString,
            ),
            'RespondToQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondToQuery,
                    request_deserializer=lms__pb2.RespondToQueryRequest.FromString,
                    response_serializer=lms__pb2.RespondToQueryReply.SerializeToString,
            ),
            'PostCourseMaterial': grpc.unary_unary_rpc_method_handler(
                    servicer.PostCourseMaterial,
                    request_deserializer=lms__pb2.PostMaterialRequest.FromString,
                    response_serializer=lms__pb2.PostMaterialResponse.SerializeToString,
            ),
            'GetCourseMaterials': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCourseMaterials,
                    request_deserializer=lms__pb2.GetCourseMaterialsRequest.FromString,
                    response_serializer=lms__pb2.GetCourseMaterialsReply.SerializeToString,
            ),
            'PostAssignment': grpc.unary_unary_rpc_method_handler(
                    servicer.PostAssignment,
                    request_deserializer=lms__pb2.PostAssignmentRequest.FromString,
                    response_serializer=lms__pb2.PostAssignmentReply.SerializeToString,
            ),
            'GetAssignments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAssignments,
                    request_deserializer=lms__pb2.GetAssignmentsRequest.FromString,
                    response_serializer=lms__pb2.GetAssignmentsReply.SerializeToString,
            ),
            'SubmitAssignment': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitAssignment,
                    request_deserializer=lms__pb2.SubmitAssignmentRequest.FromString,
                    response_serializer=lms__pb2.SubmitAssignmentReply.SerializeToString,
            ),
            'GetSubmissions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSubmissions,
                    request_deserializer=lms__pb2.GetSubmissionsRequest.FromString,
                    response_serializer=lms__pb2.GetSubmissionsReply.SerializeToString,
            ),
            'GradeSubmission': grpc.unary_unary_rpc_method_handler(
                    servicer.GradeSubmission,
                    request_deserializer=lms__pb2.GradeSubmissionRequest.FromString,
                    response_serializer=lms__pb2.GradeSubmissionReply.SerializeToString,
            ),
            'ViewGrades': grpc.unary_unary_rpc_method_handler(
                    servicer.ViewGrades,
                    request_deserializer=lms__pb2.ViewGradesRequest.FromString,
                    response_serializer=lms__pb2.ViewGradesReply.SerializeToString,
            ),
            'CheckLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckLeader,
                    request_deserializer=lms__pb2.LeaderRequest.FromString,
                    response_serializer=lms__pb2.LeaderResponse.SerializeToString,
            ),
            'RequestVote': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestVote,
                    request_deserializer=lms__pb2.RequestVoteRequest.FromString,
                    response_serializer=lms__pb2.RequestVoteResponse.SerializeToString,
            ),
            'AppendEntries': grpc.unary_unary_rpc_method_handler(
                    servicer.AppendEntries,
                    request_deserializer=lms__pb2.AppendEntriesRequest.FromString,
                    response_serializer=lms__pb2.AppendEntriesResponse.SerializeToString,
            ),
            'AnnounceLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.AnnounceLeader,
                    request_deserializer=lms__pb2.LeaderAnnouncement.FromString,
                    response_serializer=lms__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LMS', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('LMS', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LMS(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/Login',
            lms__pb2.LoginRequest.SerializeToString,
            lms__pb2.LoginResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/Logout',
            lms__pb2.LogoutRequest.SerializeToString,
            lms__pb2.StatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PostQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/PostQuery',
            lms__pb2.PostQueryRequest.SerializeToString,
            lms__pb2.PostQueryReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetQueries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/GetQueries',
            lms__pb2.GetQueriesRequest.SerializeToString,
            lms__pb2.GetQueriesReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RespondToQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/RespondToQuery',
            lms__pb2.RespondToQueryRequest.SerializeToString,
            lms__pb2.RespondToQueryReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PostCourseMaterial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/PostCourseMaterial',
            lms__pb2.PostMaterialRequest.SerializeToString,
            lms__pb2.PostMaterialResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCourseMaterials(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/GetCourseMaterials',
            lms__pb2.GetCourseMaterialsRequest.SerializeToString,
            lms__pb2.GetCourseMaterialsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PostAssignment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/PostAssignment',
            lms__pb2.PostAssignmentRequest.SerializeToString,
            lms__pb2.PostAssignmentReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAssignments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/GetAssignments',
            lms__pb2.GetAssignmentsRequest.SerializeToString,
            lms__pb2.GetAssignmentsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubmitAssignment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/SubmitAssignment',
            lms__pb2.SubmitAssignmentRequest.SerializeToString,
            lms__pb2.SubmitAssignmentReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSubmissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/GetSubmissions',
            lms__pb2.GetSubmissionsRequest.SerializeToString,
            lms__pb2.GetSubmissionsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GradeSubmission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/GradeSubmission',
            lms__pb2.GradeSubmissionRequest.SerializeToString,
            lms__pb2.GradeSubmissionReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ViewGrades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/ViewGrades',
            lms__pb2.ViewGradesRequest.SerializeToString,
            lms__pb2.ViewGradesReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CheckLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/CheckLeader',
            lms__pb2.LeaderRequest.SerializeToString,
            lms__pb2.LeaderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RequestVote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/RequestVote',
            lms__pb2.RequestVoteRequest.SerializeToString,
            lms__pb2.RequestVoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AppendEntries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/AppendEntries',
            lms__pb2.AppendEntriesRequest.SerializeToString,
            lms__pb2.AppendEntriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AnnounceLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/LMS/AnnounceLeader',
            lms__pb2.LeaderAnnouncement.SerializeToString,
            lms__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
