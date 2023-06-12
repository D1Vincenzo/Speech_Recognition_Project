from record_mic import record_audio
from api_communication import *
from word_embedding_test import *

# Record
file_name = 'output_new.wav'
record_audio(file_name)

print('Transcribe started')

# Upload & Transcribe
text = transcribe(file_name)

print('Transcribe complete:', text)

'''
# Save the transcription
save_transcription(text)
'''

# Preprocess and find most similiar command
find_the_most_similar_command(text)
