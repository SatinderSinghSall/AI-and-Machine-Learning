from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Create Flask app
app = Flask(__name__)


# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("home.html")


# ---------------- AI ASSISTANT PAGE ----------------
@app.route("/assistant")
def assistant():
    return render_template("assistant.html")


# ---------------- EMAIL PAGE ----------------
@app.route("/email")
def email():
    return render_template("email.html")


# ---------------- ASK AI ----------------
@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "Act like a helpful personal assistant"},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=512
        )

        answer = completion.choices[0].message.content.strip()

    except Exception as e:
        answer = f"Error: {str(e)}"

    return jsonify({"response": answer}), 200


# ---------------- EMAIL SUMMARY ----------------
@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("email")

    prompt = f"Summarize the following email in 2-3 sentences:\n{email_text}"

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "Act like an expert email assistant"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=512
        )

        summary = completion.choices[0].message.content.strip()

    except Exception as e:
        summary = f"Error: {str(e)}"

    return jsonify({"response": summary}), 200


if __name__ == "__main__":
    app.run(debug=True)
