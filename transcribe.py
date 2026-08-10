import whisper
from record import recording_audio

# downlaod trhe model and get result
model = whisper.load_model("base")
result = model.transcribe(recording_audio())

# print result
print(result["text"]) 