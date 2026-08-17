import whisper

def transcribe_audio(audio):
    # downlaod trhe model and get result
    model = whisper.load_model("base")
    result = model.transcribe(audio)
    
    return result["text"]