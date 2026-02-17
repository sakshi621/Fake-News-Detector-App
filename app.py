import os
import sys
import joblib
import re
import string
from flask import Flask, render_template, request, jsonify
import webview

# -------------------------------------------------
# Fix path (for normal run + PyInstaller)
# -------------------------------------------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

# -------------------------------------------------
# Load Model & Vectorizer
# -------------------------------------------------
model_path = resource_path("model.pkl")
vectorizer_path = resource_path("vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# -------------------------------------------------
# Create Flask App
# -------------------------------------------------
app = Flask(
    __name__,
    template_folder=resource_path("templates"),
    static_folder=resource_path("static")
)

# -------------------------------------------------
# Text Cleaning (MUST match training)
# -------------------------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"<.*?>+", "", text)
    text = re.sub(r"[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\w*\d\w*", "", text)
    return text

# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    news = request.form["news"]

    cleaned = clean_text(news)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    if prediction == 0:
        result = "FAKE NEWS ❌"
    else:
        result = "REAL NEWS ✅"

    return jsonify({"result": result})

# -------------------------------------------------
# Start Desktop Window
# -------------------------------------------------
if __name__ == "__main__":
    window = webview.create_window(
        "Fake News Detector",
        app,
        width=900,
        height=650
    )
    webview.start()