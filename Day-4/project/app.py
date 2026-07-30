from flask import Flask,render_template, jsonify, request
from dotenv import load_dotenv
import google.generativeai as genai
import os
load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route('/chat',methods=["POST"])
def chat():
    data=request.get_json()
    message=data.get("message")

    try:
        model=genai.GenerativeModel("gemini-flash-latest")
        response=model.generate_content(message)
        return jsonify({"response":response.text})
    except Exception as e:
        print("Gemini Error:",e)
        return jsonify({"error":str(e)})

if __name__=="__main__":
    app.run(debug=True)


# @app.route('/about')
# def about():
#     return "About Us"

# @app.route('/contact')
# def contact():
#     return "Contact Us"

app.run(debug=True)


