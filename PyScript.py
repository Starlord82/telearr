from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHATID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHATID, "text": message}
    requests.post(url, data=payload)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event = data.get("eventType", "unknown")
    if "movie" in data:
        title = data["movie"].get("title", "Unknown")
        send_telegram_message(f"🎬 Radarr: '{title}' - {event}")
    elif "series" in data:
        title = data["series"].get("title", "Unknown")
        send_telegram_message(f"📺 Sonarr: '{title}' - {event}")
    return "", 200

if __name__ == "__main__":
    print("Starting TeleArr Flask app...")
    app.run(host="0.0.0.0", port=5000)














