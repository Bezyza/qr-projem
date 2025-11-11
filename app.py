# app.py
from flask import Flask, request, redirect
import requests
from datetime import datetime

app = Flask(__name__)

# 1️⃣ Buraya kendi webhook.site adresini yapıştır:
LOGGING_URL = "https://webhook.site/31748e81-93df-4027-a93c-ff319b576fb2"

# 2️⃣ Ziyaret sonrası yönleneceği site:
FINAL_URL = "https://www.archerobotics.com/"

@app.route("/track")
def track():
    # Kullanıcı bilgilerini al
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get("User-Agent", "<bilinmiyor>")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Gönderilecek veri
    data = {
        "ip": ip,
        "user_agent": user_agent,
        "timestamp": timestamp
    }

    # Log sitesine POST isteği gönder
    try:
        requests.post(LOGGING_URL, json=data, timeout=3)
        print("Log gönderildi:", data)
    except Exception as e:
        print("Log gönderilemedi:", e)

    # Son olarak kullanıcıyı asıl siteye yönlendir
    return redirect(FINAL_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
