from audio.transcribe import transcribe_audio
from audio.record import recording_audio
from nlp.text_processor import process_text

# TESTING IMPORT
from tests.test_audio import load_audio_files

# transcribe audio and get result
text = transcribe_audio(recording_audio()) # TESTING PURPOSES: USE TRANSCRIBE_AUDIO()
print("Transcribed Text:", text)

# process the transcribed text
processed_tiers = process_text(text)
print("Processed Tiers:", processed_tiers)

# update the word frequency in the database 