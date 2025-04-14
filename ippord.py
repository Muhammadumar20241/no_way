



import telebot
from telebot import types
bot =telebot.TeleBot("7948796136:AAF3Wja3B1L3gPkHs2_jPjsNyjSW12Z1XpE")

language ="en"


@bot.message_handler(commands =['start'])
def main(message):
    global language
    
    if language =="en":
        
            
        markup2 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        btn_c1 =types.KeyboardButton("🧾List of clients")
        btn_c2 =types.KeyboardButton("💵exchange rate")
        markup2.row(btn_c2,btn_c1)
        btn_c3 =types.KeyboardButton("📩Add client")
        btn_c4 =types.KeyboardButton("⏳debtors")
        markup2.row(btn_c4,btn_c3)
        btn_c5 =types.KeyboardButton("📝order")
        btn_c6 =types.KeyboardButton("📊Administrator")
        markup2.row(btn_c5,btn_c6)
        
        
        
        
        a =message.from_user.first_name
        b =str(message.from_user.last_name)
        if b.lower().strip() =="none":
            bot.send_message(message.chat.id, f"Welcome {a}",reply_markup=markup2)
        else:
            bot.send_message(message.chat.id, f"Welcome {a} {b}",reply_markup=markup2)
            
        
    
    
    
    elif language =="uz":
        
             
        markup2 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        btn_c1 =types.KeyboardButton("🧾List of clients")
        btn_c2 =types.KeyboardButton("💵exchange rate")
        markup2.row(btn_c2,btn_c1)
        btn_c3 =types.KeyboardButton("📩Add client")
        btn_c4 =types.KeyboardButton("⏳debtors")
        markup2.row(btn_c4,btn_c3)
        btn_c5 =types.KeyboardButton("📝order")
        btn_c6 =types.KeyboardButton("📊Administrator")
        markup2.row(btn_c5,btn_c6)
        
        
        
        a =message.from_user.first_name
        b =str(message.from_user.last_name)
        if b.lower().strip() =="none":
            bot.send_message(message.chat.id, f"Xush kelibsiz {a}",reply_markup=markup2)
        else:
            bot.send_message(message.chat.id, f"Xush kelibsiz {a} {b}",reply_markup=markup2)
            
        
    
    
    
    
    elif language =="ru":
        
            
        markup2 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        btn_c1 =types.KeyboardButton("🧾List of clients")
        btn_c2 =types.KeyboardButton("💵exchange rate")
        markup2.row(btn_c2,btn_c1)
        btn_c3 =types.KeyboardButton("📩Add client")
        btn_c4 =types.KeyboardButton("⏳debtors")
        markup2.row(btn_c4,btn_c3)
        btn_c5 =types.KeyboardButton("📝order")
        btn_c6 =types.KeyboardButton("📊Administrator")
        markup2.row(btn_c5,btn_c6)
        
        
        
        
        a =message.from_user.first_name
        b =str(message.from_user.last_name)
        if b.lower().strip() =="none":
            bot.send_message(message.chat.id, f"Welcome {a}",reply_markup=markup2)
        else:
            bot.send_message(message.chat.id, f"Welcome {a} {b}",reply_markup=markup2)
            
        
    
    
    

@bot.message_handler(commands =['language'])
def main2(message):
    
    if language =="en":
            
        
        markup =types.InlineKeyboardMarkup()
        
        btn_l1 =types.InlineKeyboardButton("✅🇺🇸English",callback_data ="en")
        markup.row(btn_l1)
        btn_l2 =types.InlineKeyboardButton("🇷🇺Russian",callback_data ="ru")
        markup.row(btn_l2)
        btn_l3 =types.InlineKeyboardButton("🇺🇿Uzbek",callback_data ="uz")
        markup.row(btn_l3)
        
        
        
        
        
        bot.send_message(message.chat.id, "🌍 Please choose language",reply_markup =markup)
        
    elif language =="ru":
            
        
        markup =types.InlineKeyboardMarkup()
        
        btn_l1 =types.InlineKeyboardButton("🇺🇸English",callback_data ="en")
        markup.row(btn_l1)
        btn_l2 =types.InlineKeyboardButton("✅🇷🇺Russian",callback_data ="ru")
        markup.row(btn_l2)
        btn_l3 =types.InlineKeyboardButton("🇺🇿Uzbek",callback_data ="uz")
        markup.row(btn_l3)
        
        
        
        
        
        
        
        bot.send_message(message.chat.id, "🌍 Please choose language",reply_markup =markup)
        
    
    elif language =="uz":
            
        
        markup =types.InlineKeyboardMarkup()
        
        btn_l1 =types.InlineKeyboardButton("🇺🇸English",callback_data ="en")
        markup.row(btn_l1)
        btn_l2 =types.InlineKeyboardButton("🇷🇺Russian",callback_data ="ru")
        markup.row(btn_l2)
        btn_l3 =types.InlineKeyboardButton("✅🇺🇿Uzbek",callback_data ="uz")
        markup.row(btn_l3)
        
        
        
        
        
        bot.send_message(message.chat.id, "🌍 Please choose language",reply_markup =markup)
        
    






@bot.message_handler(func=lambda message:True)
def main4(message):
    
    if message.text.strip().lower() =="📩add client":
        
            
        markup2 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        btn_c1 =types.KeyboardButton("🧾List of clients")
        btn_c2 =types.KeyboardButton("💵exchange rate")
        markup2.row(btn_c2,btn_c1)
        btn_c3 =types.KeyboardButton("📩Add client")
        btn_c4 =types.KeyboardButton("⏳debtors")
        markup2.row(btn_c4,btn_c3)
        btn_c5 =types.KeyboardButton("📝order")
        btn_c6 =types.KeyboardButton("📊Administrator")
        markup2.row(btn_c5,btn_c6)
        
        
        def user_id(message):
            global a
            a =str(message.text.strip().lower())
            bot.send_message(message.chat.id, "please enter name of client")
            bot.register_next_step_handler(message, user_name)
            
        def user_name(message):
            global a, b
            b =str(message.text.strip().lower())
            bot.send_message(message.chat.id, "enter surname of client")
            bot.register_next_step_handler(message, user_surname)
            
        def user_surname(message):
            global a, b, c
            c =str(message.text.strip().lower())
            
            
            try:
                connection = pymysql.connect(
                    host='localhost',
                    user='muhamm37_muhamm',
                    password='umar022004',
                    database='muhamm37_muhammad',
                    port=3306,
                    cursorclass=pymysql.cursors.DictCursor
                )
                print("successfully connected...")
                print('#' * 20)
                try:
                    with connection.cursor() as cursor:
                        create_table_query = f"CREATE TABLE IF NOT EXISTS all_clients (id int AUTO_INCREMENT,id varchar(100), name varchar(150), surname varchar(150), PRIMARY KEY(id));"
                        cursor.execute(create_table_query)
                        print("table created....")

                        select_query = f"SELECT * FROM all_clients WHERE id = %s"
                        cursor.execute(select_query, (a,))
                        result = cursor.fetchone()

                        if result:
                            bot.send_message(message.chat.id, "Siz allaqachon ro'yxatdan o'tgansiz!")
                        else:
                            insert_query = f"INSERT INTO all_students(chat_id, student_id) VALUES (%s, %s)"
                            cursor.execute(insert_query, (a, r))
                            connection.commit()
                            bot.send_message(message.chat.id, "Siz roʻyxatdan oʻtdingiz !")

                finally:
                    connection.close()

            except Exception as ex:
                print("connection refused...")
                print(ex)
                


            
            
            
        
        
        
        
        
        
        
        
        
        
        bot.send_message(message.chat.id, "please enter id of a client",reply_markup=markup2)
        bot.register_next_step_handler(message, user_id)
        
        
    

















@bot.callback_query_handler(func =lambda callback: True)
def main3(callback):
    if callback.data =="en":
        language ="en"
            
        markup2 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        btn_c1 =types.KeyboardButton("🧾List of clients")
        btn_c2 =types.KeyboardButton("💵exchange rate")
        markup2.row(btn_c2,btn_c1)
        btn_c3 =types.KeyboardButton("📩Add client")
        btn_c4 =types.KeyboardButton("⏳debtors")
        markup2.row(btn_c4,btn_c3)
        btn_c5 =types.KeyboardButton("📝order")
        btn_c6 =types.KeyboardButton("📊Administrator")
        markup2.row(btn_c5,btn_c6)
        
        
        
        
        markup =types.InlineKeyboardMarkup()
        
        btn_l1 =types.InlineKeyboardButton("✅🇺🇸English",callback_data ="en")
        markup.row(btn_l1)
        btn_l2 =types.InlineKeyboardButton("🇷🇺Russian",callback_data ="ru")
        markup.row(btn_l2)
        btn_l3 =types.InlineKeyboardButton("🇺🇿Uzbek",callback_data ="uz")
        markup.row(btn_l3)
        
        bot.edit_message_text("🌍 Please choose language",callback.message.chat.id, callback.message.message_id,reply_markup=markup)
        bot.send_message(callback.message.chat.id, "You have selected English language",reply_markup =markup2)
    
    elif callback.data =="ru":
        language ="ru"
        
             
        markup2 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        btn_c1 =types.KeyboardButton("🧾List of clients")
        btn_c2 =types.KeyboardButton("💵exchange rate")
        markup2.row(btn_c2,btn_c1)
        btn_c3 =types.KeyboardButton("📩Add client")
        btn_c4 =types.KeyboardButton("⏳debtors")
        markup2.row(btn_c4,btn_c3)
        btn_c5 =types.KeyboardButton("📝order")
        btn_c6 =types.KeyboardButton("📊Administrator")
        markup2.row(btn_c5,btn_c6)
        
        
        
        markup =types.InlineKeyboardMarkup()
        
        btn_l1 =types.InlineKeyboardButton("🇺🇸English",callback_data ="en")
        markup.row(btn_l1)
        btn_l2 =types.InlineKeyboardButton("✅🇷🇺Russian",callback_data ="ru")
        markup.row(btn_l2)
        btn_l3 =types.InlineKeyboardButton("🇺🇿Uzbek",callback_data ="uz")
        markup.row(btn_l3)
        
        
        bot.edit_message_text("🌍 Пожалуйста, выберите язык",callback.message.chat.id, callback.message.message_id,reply_markup=markup)
        bot.send_message(callback.message.chat.id, "Вы выбрали Pyccкий язык",reply_markup =markup2)

        
        
     
    elif callback.data =="uz":
        language ="uz"
        
        
               
        markup2 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        btn_c1 =types.KeyboardButton("🧾List of clients")
        btn_c2 =types.KeyboardButton("💵exchange rate")
        markup2.row(btn_c2,btn_c1)
        btn_c3 =types.KeyboardButton("📩Add client")
        btn_c4 =types.KeyboardButton("⏳debtors")
        markup2.row(btn_c4,btn_c3)
        btn_c5 =types.KeyboardButton("📝order")
        btn_c6 =types.KeyboardButton("📊Administrator")
        markup2.row(btn_c5,btn_c6)
        
        
        
        
        markup =types.InlineKeyboardMarkup()
        
        btn_l1 =types.InlineKeyboardButton("🇺🇸English",callback_data ="en")
        markup.row(btn_l1)
        btn_l2 =types.InlineKeyboardButton("🇷🇺Russian",callback_data ="ru")
        markup.row(btn_l2)
        btn_l3 =types.InlineKeyboardButton("✅🇺🇿Uzbek",callback_data ="uz")
        markup.row(btn_l3)
        
        
        bot.edit_message_text("🌍 Iltimos, tilni tanlang",callback.message.chat.id, callback.message.message_id,reply_markup=markup)
        bot.send_message(callback.message.chat.id, "Siz O'zbek tilini tanladingiz",reply_markup =markup2)

      
    
    










bot.polling(none_stop=True)




















