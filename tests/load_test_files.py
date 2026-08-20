import os
import csv

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

def load_files(audio_or_text):
    files = []
    if audio_or_text == "text":
        valid_file_formats = (".txt")
    elif audio_or_text == "audio":
        valid_file_formats = (".mp3", ".wav", ".flac")
    
    for file in os.listdir(os.path.join(FOLDER_PATH, "test_files")):
        if file.endswith(valid_file_formats):
            print(file)
            files.append(os.path.join(FOLDER_PATH, "test_files", file))
    
    return files