from speech_to_text import Transcriber
from word_embedding import find_the_most_similar_command

transcriber = Transcriber()
while True:
    input()
    for transcript in transcriber.start():
        if find_the_most_similar_command(transcript):
            print("Command received:", find_the_most_similar_command(transcript)) 