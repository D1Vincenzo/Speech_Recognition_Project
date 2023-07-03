import pyaudio
import wave
import threading

FRAME_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

def record_audio(filename):
    try:
        p = pyaudio.PyAudio()

        stream = p.open(
            format = FORMAT,
            channels = CHANNELS,
            rate = RATE,
            input = True,
            frames_per_buffer = FRAME_PER_BUFFER
        )

        print('Start recording...')

        frames = []
        is_recording = True

        def check_input():
            nonlocal is_recording
            input("Press Enter to stop recording\n")
            is_recording = False

        thread = threading.Thread(target=check_input)
        thread.start()

        while is_recording:
            data = stream.read(FRAME_PER_BUFFER)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        obj = wave.open(filename, 'wb')
        obj.setnchannels(CHANNELS)
        obj.setsampwidth(p.get_sample_size(FORMAT))
        obj.setframerate(RATE)
        obj.writeframes(b''.join(frames))
        obj.close()

    except Exception as e:
        print("Exception: ", str(e))

