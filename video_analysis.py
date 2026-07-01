import cv2
import json
import google.generativeai as genai
from speech_to_text_video import speech_to_text_video

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_video(video_path):

    cap = cv2.VideoCapture(video_path)

    total_frames = 0
    fps = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        total_frames += 1

    cap.release()

    duration = total_frames / fps if fps > 0 else 0

    transcript = speech_to_text_video(video_path)
    print("\n========== TRANSCRIPT ==========")
    print(transcript)
    print("================================")

    prompt = f"""
You are an expert AI Presentation Coach.

Presentation Transcript:
{transcript}

Presentation Duration:
{duration:.2f} seconds

Analyze the presentation.

Consider:
- Clarity
- Confidence
- Communication
- Fluency
- Structure
- Vocabulary
- Professionalism

Return ONLY valid JSON.

{{
"score":"",
"confidence":"",
"nervousness":"",
"communication":"",
"strengths":[],
"improvements":[],
"feedback":""
}}
Return ONLY valid JSON.


Rules:
- score must be an integer from 1 to 10 only.
- confidence must be an integer from 1 to 10 only.
- nervousness must be an integer from 1 to 10 only.
- communication must be an integer from 1 to 10 only.
- Do NOT use /100.
- Do NOT use percentages.
- Do NOT write 'Low', 'High', or 'Excellent'.
- Return ONLY JSON and nothing else.
"""

    response = model.generate_content(prompt)

    text = response.text.replace("```json","").replace("```","")

    return json.loads(text)