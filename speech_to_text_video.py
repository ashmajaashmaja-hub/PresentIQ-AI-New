import speech_recognition as sr
from moviepy.editor import VideoFileClip
import os

def speech_to_text_video(video_path):
    recognizer = sr.Recognizer()

    # Extract audio from video
    audio_path = "temp_audio.wav"

    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, logger=None)

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        transcript = recognizer.recognize_google(audio)
    except Exception:
        transcript = "Speech could not be recognized."

    if os.path.exists(audio_path):
        os.remove(audio_path)

    return transcript