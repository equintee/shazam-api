from concurrent import futures
import grpc
from service.music_recognition_pb2_grpc import add_MusicRecoginitonServiceServicer_to_server
from service.music_recogniton_service import MusicRecognitionService

def serve():
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=10))

    server.add_insecure_port('[::]:50001')
    add_MusicRecoginitonServiceServicer_to_server(MusicRecognitionService(), server)
    server.start()
    print("Server started on port 50001")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
