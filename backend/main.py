from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import os
import re

app = FastAPI(title="UPI Scam Detector API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "..", "model", "model.pkl")
vectorizer_path = os.path.join(script_dir, "..", "model", "vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

history = []


class Message(BaseModel):
    text: str


def check_rule_based_flags(text: str):
    flags = []
    text_lower = text.lower()

    suspicious_keywords = [
        "kyc", "click here", "click to claim", "verify now", "urgent",
        "account blocked", "account suspended", "otp", "refund",
        "lottery", "prize", "winner", "loan approved", "cashback",
        "claim now", "act now", "limited time",
    ]
    for keyword in suspicious_keywords:
        if keyword in text_lower:
            flags.append(f"Contains suspicious keyword: '{keyword}'")

    if re.search(r"(bit\.ly|tinyurl|t\.co|\.tk|\.xyz|\.info)", text_lower):
        flags.append("Contains a suspicious or shortened link")

    return flags


@app.get("/")
def root():
    return {"message": "UPI Scam Detector API is running"}


@app.post("/analyze")
def analyze_message(msg: Message):
    text = msg.text

    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    probabilities = model.predict_proba(vec)[0]
    confidence = round(max(probabilities) * 100, 2)

    flags = check_rule_based_flags(text)

    final_label = prediction
    if flags and prediction == "safe":
        final_label = "suspicious"

    result = {
        "message": text,
        "prediction": final_label,
        "confidence": confidence,
        "reasons": flags if flags else ["No suspicious patterns detected"],
    }

    history.append(result)

    return result


@app.get("/stats")
def get_stats():
    total = len(history)
    scam_count = sum(1 for h in history if h["prediction"] == "scam")
    suspicious_count = sum(1 for h in history if h["prediction"] == "suspicious")
    safe_count = sum(1 for h in history if h["prediction"] == "safe")

    return {
        "total_scanned": total,
        "scam_detected": scam_count,
        "suspicious_detected": suspicious_count,
        "safe_messages": safe_count,
    }


@app.get("/history")
def get_history():
    return {"history": history[::-1]}