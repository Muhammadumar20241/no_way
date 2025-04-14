from flask import Flask, request
import telebot

TOKEN = '7948796136:AAF3Wja3B1L3gPkHs2_jPjsNyjSW12Z1XpE'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Bot is running."

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return '', 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, I am alive!")

# Set webhook
import requests
bot.remove_webhook()
bot.set_webhook(url=f'https://Muhammadumar20241/no_way/{TOKEN}')
