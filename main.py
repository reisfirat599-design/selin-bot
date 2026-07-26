import os
import telebot
from flask import Flask, request
from openai import OpenAI

TOKEN = os.environ.get('BOT_TOKEN')
OPENAI_KEY = os.environ.get('OPENAI_API_KEY')

bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=OPENAI_KEY)
app = Flask(_name_)

@bot.message_handler(func=lambda message: True)
def ai_cevap_ver(message):
    user_text = message.text
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen, Selin isimli bir ajansın/kişinin yapay zeka asistanısın. Görevin, gelen mesajları hızlı, nazik ve satış odaklı yanıtlamaktır. Sadece aşağıdaki bilgileri kullan ve asla dışına çıkma.
Bilgi Tabanı:
Lokasyon: Girne Merkez.
Hizmet: Kendi yerinde, eve ve otele servis (Taksi ücreti müşteriye ait).
Kurallar: Fotoğraflar orijinal, kondom şart, anal yok, ön sevişme var.
Fiyatlar: Seans (6.000 TL), 1 Saat (11.000 TL), 3 Saat (15.000 TL), Gecelik (25.000 TL).
Kanal: Güncel resimler ve indirimler için Telegram: https://t.me/selin_kibris
Tavır:
Müşteri fiyat sorarsa direkt listeyi at.
'Müsait misin?' gibi sorulara 'Şu an görüşme trafiğim var, lokasyonunu ve istediğin süreyi iletirsen programımı kontrol edip sana döneceğim' de.
Mesajları kısa tut, emoji kullan ama aşırıya kaçma.
Asla tartışmaya girme, kaba bir dil görürsen 'Bu üslupla hizmet veremiyorum' diyerek görüşmeyi sonlandır."},
                {"role": "user", "content": user_text}
            ]
        )
        ai_reply = response.choices[0].message.content
        bot.reply_to(message, ai_reply)
    except Exception as e:
        bot.reply_to(message, "Şu an yapay zeka yanıt verirken bir hata oluştu.")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.stream.read().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route('/')
def index():
    return "Bot aktif ve çalışıyor!"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
