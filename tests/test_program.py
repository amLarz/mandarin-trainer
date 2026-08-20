from main import main
from tests.audio_test import load_audio_files

def test_main():
    audio_files = load_audio_files()
    
    for audio_file in audio_files:
        print(f"Testing with audio file: {audio_file}")
        main()  # Call the main function for each audio file
        
    return 0 

test_main()