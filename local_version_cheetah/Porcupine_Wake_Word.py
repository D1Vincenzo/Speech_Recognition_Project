import struct
import pvporcupine
import pyaudio
from AccessKey import ACCESS_KEY

porcupine = pvporcupine.create(
    access_key = ACCESS_KEY,
    keywords = ["picovoice", "bumblebee"])

def get_next_audio_frame():
    myaudio = pyaudio.PyAudio()
    stream = myaudio.open(
        input_device_index=0,
        rate = porcupine.sample_rate,
        channels = 1,
        format = pyaudio.paInt16,
        input = True,
        frames_per_buffer = porcupine.frame_length)
    while True:
        audio_obj = stream.read(porcupine.frame_length, exception_on_overflow=False)
        audio_obj_unpacked = struct.unpack_from("h" * porcupine.frame_length, audio_obj)
        audio_frame = audio_obj_unpacked

        keyword_index = porcupine.process(audio_frame)
        if keyword_index >= 0:
            print("Jungle")

get_next_audio_frame()
porcupine.delete()


