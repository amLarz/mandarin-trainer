import os

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
def load_audio_files():
    for file in os.listdir(FOLDER_PATH):
        if file.endswith((".mp3", ".wav", ".m4a", ".flac")):
            file_path = os.path.join(FOLDER_PATH, 'audio-test', file)
            print(file_path)
    
    return file_path