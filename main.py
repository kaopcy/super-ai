import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("สภานที่ท่องเที่ยวเด็ดๆในไทย, ตอบรูปแบบแชทบอท")

print("====start====")
print(response.text)
print("====end====")