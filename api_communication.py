import requests
from api_secrets import API_KEY_ASSEMBLYAI
import time


# Upload to assemblyai
base_url = "https://api.assemblyai.com/v2"

headers = {
    "authorization": API_KEY_ASSEMBLYAI
}

def upload_audio(file_name):
    with open(file_name, "rb") as f:
        response = requests.post(base_url + "/upload", headers=headers, data=f)
    return response.json()["upload_url"]

def start_transcription(upload_url):
    data = {
        "audio_url": upload_url
    }
    url = base_url + "/transcript"
    response = requests.post(url, json=data, headers=headers)
    return response.json()['id']

def wait_for_transcription(transcript_id):
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    while True:
        transcription_result = requests.get(polling_endpoint, headers=headers).json()
        if transcription_result['status'] == 'completed':
            return transcription_result['text']
        elif transcription_result['status'] == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")
        else:
            print('Waiting for 3 more seconds...')
            time.sleep(3)

def save_transcription(transcription_text):
    with open('transcription.txt', 'w') as f:
        f.write(transcription_text)
    print('Transcription saved')