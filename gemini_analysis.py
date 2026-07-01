import google.generativeai as genai

import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

speech = input("Enter Presentation Text:\n")

prompt = f"""
You are an AI Presentation Coach.

Analyze this presentation.

Presentation:

{speech}

Give:

1. Overall Score /100

2. Confidence Level

3. Estimated Nervousness

4. Speaking Quality

5. Communication

6. Improvements

7. Final Feedback
"""

response = model.generate_content(prompt)

print(response.text)