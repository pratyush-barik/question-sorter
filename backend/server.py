from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import base64
import os

from pipeline import run_pipeline

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

CORS(app)


# 🔹 Serve frontend
@app.route("/")
def home():
    return render_template("index.html")


# 🔹 Main processing API
@app.route("/process", methods=["POST"])
def process():
    try:
        data = request.get_json()

        syllabus = data.get("syllabus", "")
        questions = data.get("questions", "")

        if not syllabus or not questions:
            return jsonify({"error": "Missing syllabus or questions"}), 400

        # Run NLP pipeline
        output_path = run_pipeline(syllabus, questions)

        # Convert PDF to base64
        with open(output_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()

        return jsonify({"file": encoded})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🔹 Health check (optional but useful)
@app.route("/health")
def health():
    return "OK"


# 🔹 Run app (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)