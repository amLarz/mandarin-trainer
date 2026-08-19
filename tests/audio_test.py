import os

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

def load_audio_files():
    
    valid_file_formats = (".mp3", ".wav", ".flac")
    
    for file in os.listdir(os.path.join(FOLDER_PATH, "audio_files")):
        if file.endswith(valid_file_formats):
            print(file)
            return os.path.join(FOLDER_PATH, file)
        
load_audio_files()