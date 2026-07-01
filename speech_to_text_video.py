import whisper

# Load the model once
model = whisper.load_model("base")

def speech_to_text_video(video_path):

    result = model.transcribe(video_path)

    transcript = result["text"]

    return transcript