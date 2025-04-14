
import telebot
from telebot import types


from flask import Flask, request
app = Flask(__name__)
application = app





@app.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
        
@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://bot.muhammadumarkoziev.uz/bot") 
    return "!", 200

BOT_TOKEN = '7948796136:AAF3Wja3B1L3gPkHs2_jPjsNyjSW12Z1XpE'

bot = telebot.TeleBot(BOT_TOKEN)




@bot.message_handler(commands =['start'])
def main(message):
    
    markup1 =types.ReplyKeyboardMarkup(resize_keyboard =True)
    btn1 =types.KeyboardButton("📜Listings")
    btn2 =types.KeyboardButton("🏠Housing")
    markup1.row(btn1)
    markup1.row(btn2)
    
    
    
    bot.send_message(message.chat.id, "🌚Hello\n🌝This is bot for posting rent houses", reply_markup=markup1)














if __name__ == "__main__":
   bot.polling(none_stop=True)










