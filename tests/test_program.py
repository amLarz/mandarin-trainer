from main import main
from tests.load_test_files import load_files

def test_main():
    audio_or_text = input("Do you want to test with audio files or text? (Enter 'audio' or 'text'): ").strip().lower()
    
    files = load_files(audio_or_text)
    print(files)
    i = 0
    for file in files:
        i += 1
        print(f"TEST {i}--------------------------------------------------") 
        main(file, input_type=audio_or_text)  # Call the main function for each audio file
        print("\n\n") # Add a newline for better readability between tests
        
    return 0 

test_main()