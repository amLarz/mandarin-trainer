from audio.transcribe import transcribe_audio
from audio.record import recording_audio
from data.db import save_to_database
from nlp.text_processor import process_text

def main():
    # transcribe audio and get result
    text = transcribe_audio(recording_audio()) # TESTING PURPOSES: USE TRANSCRIBE_AUDIO()
    print("Transcribed Text:", text)

    # process the transcribed text
    processed_text = process_text(text)
    print("Processed Text:", processed_text)

    # update the word frequency in the database 
    print(save_to_database(processed_text))
    
if __name__ == "__main__":
    main()