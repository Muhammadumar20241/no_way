import os
from flask import Flask, request
import telebot
from telebot import types

TOKEN = '7948796136:AAF3Wja3B1L3gPkHs2_jPjsNyjSW12Z1XpE'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# This is needed for Render to run your Flask app
application = app

@app.route('/', methods=['GET'])
def index():
    return "Bot is running."

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook_handler():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Invalid content type', 400

@app.route("/bot", methods=['POST'])
def getMessage(): # This route seems redundant with the webhook_handler
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/set_webhook", methods=["GET", "POST"])
def set_webhook():
    webhook_url = f'https://{os.environ.get("RENDER_EXTERNAL_HOSTNAME")}/bot' # Use /bot as the endpoint
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
    return "Webhook set!", 200

@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📜Listings")
    btn2 = types.KeyboardButton("🏠Housing")
    markup1.row(btn1)
    markup1.row(btn2)
    bot.send_message(message.chat.id, "🌚Hello\n🌝This is bot for posting rent houses", reply_markup=markup1)

if __name__ == "__main__":
    # Run the Flask app on the port provided by the environment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
