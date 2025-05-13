# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-2.0-flash")
# response = model.generate_content("สภานที่ท่องเที่ยวเด็ดๆในไทย, ตอบรูปแบบแชทบอท")

# print("====start====")
# print(response.text)
# print("====end====")

from flask import Flask, request, jsonify, render_template
import requests
import uuid
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/send-line-message", methods=["POST"])
def send_line_message():
    # Replace these values with actual values or pass them via POST body or environment
    channel_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_token}",
        "X-Line-Retry-Key": str(uuid.uuid4())
    }

    payload = {
        "messages": [
            {"type": "text", "text": "ควยไรไอหน้าโง่"},
        ]
    }

    line_api_url = "https://api.line.me/v2/bot/message/broadcast"
    response = requests.post(line_api_url, headers=headers, json=payload)

    return jsonify({
        "status_code": response.status_code,
        "response": response.json() if response.content else "No content"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)