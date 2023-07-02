import pvleopard
def transcribe(file_name):
    handle = pvleopard.create(access_key='a238spA3P91ZXivmxwOpbj4tsrenE35mZNzFfbH4aHPw4Yv+A8c4WA==')

    transcription_text, words = handle.process_file(file_name)

    handle.delete()

    return transcription_text
