import whisper
from record import recording_audio

def transcribe_audio():
    # downlaod trhe model and get result
    model = whisper.load_model("base")
    result = model.transcribe(recording_audio())

    return result["text"]