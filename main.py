from transcribe import transcribe_audio
from text_processor import classify_words


# transcribe audio and get result
text = transcribe_audio()
print("Transcribed Text:", text)

# process the transcribed text
processed_text = classify_words(text)
print("Processed Text:", processed_text)