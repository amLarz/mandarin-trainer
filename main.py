from transcribe import transcribe_audio
from record import recording_audio
from text_processor import process_text

# TESTING IMPORT
from testing.test_audio import load_audio_files

# transcribe audio and get result
text = transcribe_audio(recording_audio()) # TESTING PURPOSES: USE TRANSCRIBE_AUDIO()
print("Transcribed Text:", text)

# process the transcribed text
processed_tiers = process_text(text)
print("Processed Tiers:", processed_tiers)

# update the word frequency in the database 