from transcribe import transcribe_audio
from text_processor import process_text
from frequency import update_database


# transcribe audio and get result
text = "I run everyday before going to school. 1, 2, 3, 4, 5" # TESTING PURPOSES: USE TRANSCRIBE_AUDIO()
print("Transcribed Text:", text)
# process the transcribed text
processed_tiers = process_text(text)
print("Processed Tiers:", processed_tiers)

# update the word frequency in the database 