from flask import Flask, request, redirect
import requests
from datetime import datetime

app = Flask(__name__)

# 🔗 Webhook.site adresin (logların düşeceği yer)
LOGGING_URL = "https://webhook.site/31748e81-93df-4027-a93c-ff319b576fb2"

# 🌐 Ziyaretçi yönlendirme adresi
FINAL_URL = "https://www.archerobotics.com/"

@app.route("/track")
def track():
    print("✅ /track rotası çağrıldı")  # Takip başlatıldı

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get("User-Agent", "<bilinmiyor>")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "ip": ip,
        "user_agent": user_agent,
        "timestamp": timestamp
    }

    try:
        requests.post(LOGGING_URL, json=data, timeout=3)
        print("📨 Log gönderildi:", data)
    except Exception as e:
        print("❌ Log gönderilemedi:", e)

    print("➡️ Şimdi yönlendiriliyor:", FINAL_URL)
    return redirect(FINAL_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

