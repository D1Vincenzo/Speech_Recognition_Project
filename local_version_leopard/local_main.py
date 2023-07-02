from local_record_mic import record_audio
from local_voice_to_text import *
from local_word_embedding_test import *

# Record
file_name = 'output_new.wav'
record_audio(file_name)

print('Transcribe started')

# Upload & Transcribe
text = transcribe(file_name)

print('Transcribe complete:', text)

'''
# Save the transcription in txt
save_transcription(text)
'''

# Preprocess & find most similiar command
if find_the_most_similar_command(text):
    print("Command received:", find_the_most_similar_command(text)) 
else: 
    print("Command not recognized. Please try again.")
