import whisper
from record import recording_audio
from test_audio import load_audio_files

def transcribe_audio():
    # downlaod trhe model and get result
    model = whisper.load_model("base")
    result = model.transcribe(recording_audio())

    return result["text"]

# testing purposes
def transcribe_test():
    # downlaod trhe model and get result
    model = whisper.load_model("base")
    result = model.transcribe(load_audio_files())
    
    return result["text"]