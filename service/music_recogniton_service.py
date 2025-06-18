
from service.music_recognition_pb2_grpc import MusicRecoginitonServiceServicer
import service.music_recognition_pb2 as pb2
from shazamio import Shazam
import asyncio
class MusicRecognitionService(MusicRecoginitonServiceServicer):
    def RecognizeSong(self, request, context):
        shazam = Shazam()
        loop = asyncio.new_event_loop()
        song = loop.run_until_complete(shazam.recognize(request.audio_clip))
        a =  pb2.RecognizeSongResponse(song_name="Sample Song Name", artist="Sample Artist")
        return a