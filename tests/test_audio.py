import whisper
import os

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

def load_audio_files():
    
    valid_file_formats = (".mp3", ".wav", ".flac")
    
    for file in os.listdir(os.path.join(FOLDER_PATH)):
        if file.endswith(valid_file_formats):
            return os.path.join(FOLDER_PATH, file)