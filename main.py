from transcribe import transcribe_audio, transcribe_test
from text_processor import process_text
from frequency import update_database


# transcribe audio and get result
text = transcribe_test() # TESTING PURPOSES: USE TRANSCRIBE_AUDIO()
print("Transcribed Text:", text)

# process the transcribed text
processed_tiers = process_text(text)
print("Processed Tiers:", processed_tiers)

# update the word frequency in the database
update_database(processed_tiers)
