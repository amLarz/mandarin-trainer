import whisper
from test_path import load_audio_files

audio_file = load_audio_files()

model = whisper.load_model("turbo")
result = model.transcribe(audio_file)

print(result["text"])