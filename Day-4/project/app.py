from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/chat', methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "No message provided."})

    if not API_KEY:
        return jsonify({"response": "Set GEMINI_API_KEY to enable AI replies in deployment."})

    try:
        model = genai.GenerativeModel("gemini-flash-latest")
        response = model.generate_content(message)
        reply = getattr(response, "text", None) or str(response)
        return jsonify({"response": reply})
    except Exception as e:
        print("Gemini Error:", e)
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)


