import os
import telebot
from flask import Flask, request

# BotFather'dan aldığın token'ı buraya veya Railway ayarlarına ekleyeceğiz
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

app = Flask(_name_)

# Kullanıcı Telegram'dan bir şey yazdığında burası çalışır
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_text = message.text
    chat_id = message.chat.id
    
    # Şimdilik kullanıcının yazdığı mesaja test amaçlı yanıt veriyor
    # Buraya ileride OpenAI (Yapay Zeka) entegrasyonunu ekleyeceğiz!
    bot.reply_to(message, f"Mesajın alındı: {user_text}")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.stream.read().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route('/')
def index():
    Statu = "Bot aktif ve çalışıyor!"
    return Statu

if _name_ == "_main_":
    # Telegram webhook ayarını otomatik yapıyoruz
    bot.remove_webhook()
    # Railway'in vereceği adresi buraya bağlayacağız
    # Not: railway canlıya aldığında webhook'u domain üzerinden tetikleyeceğiz
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
