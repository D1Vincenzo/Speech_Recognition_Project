from speech_to_text import listen_and_transcribe
from word_embedding import find_the_most_similar_command

for transcript in listen_and_transcribe():
#    print(transcript)
    if find_the_most_similar_command(transcript):
        print("Command received:", find_the_most_similar_command(transcript)) 