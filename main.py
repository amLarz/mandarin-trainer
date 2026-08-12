from transcribe import transcribe_audio
from text_processor import process_text


# transcribe audio and get result
text = transcribe_audio()
print("Transcribed Text:", text)

# process the transcribed text
processed_tiers = process_text(text)
print("Processed Tiers:", processed_tiers)