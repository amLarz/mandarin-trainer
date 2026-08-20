from main import main
from tests.load_test_files import load_files

def test_main():
    audio_or_text = input("Do you want to test with audio files or text? (Enter 'audio' or 'text'): ").strip().lower()
    
    files = load_files(audio_or_text)
    print(files)
    for file in files:
        print(f"Testing with audio file: {file}")
        main(file)  # Call the main function for each audio file
        
    return 0 

test_main()