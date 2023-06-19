# Speech_Recognition_Project
Library used: gensim numpy pyaudio wave time requests

The program aims to transcribe spoken language into written text and then identify specific commands within the transcribed text. It is implemented in Python and uses the AssemblyAI API for speech-to-text transcription.

### **Key Components**

The program is divided into four Python modules, each responsible for a specific task:

### **1. main.py**

This is the entry point of the project. It initiates the audio recording, transcribes the recorded audio, and then processes the transcribed text to identify any commands.

### **2. record_mic.py**

This module is responsible for recording audio from the microphone. It uses the PyAudio library to record a short audio clip and saves it as a .wav file.

### **3. api_communication.py**

This module handles communication with the AssemblyAI API. It uploads the recorded audio file to AssemblyAI, initiates the transcription process, and retrieves the transcription once it's complete.

The transcriptions are returned as plain text. The text can optionally be saved to a file.

### **4. word_embedding_test.py**

This module processes the transcribed text to identify commands. It uses a pre-trained Word2Vec model to vectorize both the transcribed text and a set of known commands.

The cosine similarity between the vectorized transcription and each known command is calculated. The command with the highest similarity is identified as the command present in the transcribed text.

### **Workflow**

1. The program starts recording audio from the microphone when **`main.py`** is run.
2. The recorded audio is saved as a .wav file.
3. **`api_communication.py`** uploads the .wav file to AssemblyAI and initiates the transcription process.
4. The transcription is retrieved from AssemblyAI and returned as plain text.
5. **`word_embedding_test.py`** processes the transcribed text to identify any commands.
6. If a command is identified, it is printed to the console. If no command is identified, the program prints a message indicating that no command was recognized.

<img width="485" alt="image" src="https://github.com/D1Vincenzo/Speech_Recognition_Project/assets/106391907/00afa74e-80b0-4f17-a458-d5abb85e8504">

