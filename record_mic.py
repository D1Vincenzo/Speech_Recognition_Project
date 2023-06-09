import pyaudio
import wave

FRAME_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

def record_audio(filename, seconds=5):
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
        for i in range(0, int(RATE/FRAME_PER_BUFFER*seconds)):
            data = stream.read(FRAME_PER_BUFFER)
            frames.append(data)
            # Timer
            remaining = seconds - (i * FRAME_PER_BUFFER / RATE)
            print(f"Time remaining: {remaining:.2f}")

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

