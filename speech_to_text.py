import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:

    print("🎤 Speak now...")

    recognizer.adjust_for_ambient_noise(source, duration=1)

    audio = recognizer.listen(source)

print("🤖 Converting speech to text...")

try:
    text = recognizer.recognize_google(audio)

    print("\nTranscript:")
    print(text)

except sr.UnknownValueError:
    print("Sorry, I couldn't understand your speech.")

except sr.RequestError:
    print("Could not connect to Google Speech Recognition.")