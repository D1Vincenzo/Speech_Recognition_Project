import pvleopard
def transcribe(file_name):
    handle = pvleopard.create(
    access_key='a238spA3P91ZXivmxwOpbj4tsrenE35mZNzFfbH4aHPw4Yv+A8c4WA==',
    model_path='local_version_leopard/robot_commands-leopard-v1.2.0-23-07-03--07-27-53.pv')

    transcription_text, words = handle.process_file(file_name)

    handle.delete()

    return transcription_text
