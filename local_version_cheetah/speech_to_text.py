from pvrecorder import PvRecorder
import pvcheetah
from AccessKey import ACCESS_KEY
import threading

# Hardcoded values
library_path = None
model_path = None
endpoint_duration_sec = 1.0
enable_automatic_punctuation = True
audio_device_index = -1

def listen_and_transcribe():
    cheetah = pvcheetah.create(
        access_key=ACCESS_KEY,
        library_path=library_path,
        model_path=model_path,
        endpoint_duration_sec=endpoint_duration_sec,
        enable_automatic_punctuation=enable_automatic_punctuation)

    stop_flag = threading.Event()

    def check_stop():
        input()
        stop_flag.set()

    threading.Thread(target=check_stop).start()

    try:

        recorder = PvRecorder(device_index=audio_device_index, frame_length=cheetah.frame_length)
        recorder.start()
        print('Listening... (press Ctrl+C or Enter to stop)')

        try:
            text = ''
            while not stop_flag.is_set():
                partial_transcript, is_endpoint = cheetah.process(recorder.read())
                if partial_transcript:
                    text += partial_transcript
                if is_endpoint:
                    yield text+cheetah.flush()
                    text = ''
        finally:
            print()
            recorder.stop()

    except KeyboardInterrupt:
        pass
    finally:
        cheetah.delete()

if __name__ == "__main__":
    listen_and_transcribe()
    for transcript in listen_and_transcribe():
        print(transcript)