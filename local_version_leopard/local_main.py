from local_record_mic import record_audio
from local_voice_to_text import *
from local_word_embedding_test import *
import time
# Record
file_name = 'output_new.wav'
record_audio(file_name)

print('Transcribe started')

# Count the transcribing time
start_time = time.time()

# Upload & Transcribe
text = transcribe(file_name)

end_time = time.time()

print('Transcribe complete:{} \n Transcription time:{} seconds'.format(text, end_time - start_time))

'''
# Save the transcription in txt if needed
save_transcription(text)
'''

# Preprocess & find most similiar command
if find_the_most_similar_command(text):
    print("Command received:", find_the_most_similar_command(text)) 
else: 
    print("Command not recognized. Please try again.")
