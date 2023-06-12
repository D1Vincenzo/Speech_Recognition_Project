from record_mic import record_audio
from api_communication import *
from word_embedding_test import *

# Record
file_name = 'output_new.wav'
record_audio(file_name)

print('Transcribe started')

# Upload & Transcribe
upload_url = upload_audio(file_name)
transcript_id = start_transcription(upload_url)
transcription_text = wait_for_transcription(transcript_id)

print('Transcribe complete:')

print(transcription_text)

# Save the transcription
save_transcription(transcription_text)

