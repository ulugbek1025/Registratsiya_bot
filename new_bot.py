import telebot
from telebot import types
from string import Template
bot=telebot.TeleBot('1798929012:AAECpRSEsUqv_A6DRJfdFMiwxGm6L0GAgz4')
user_dict = {}
class User:
    def __init__(self,city):
        self.city=city

        keys = ['jins','FIO','phone',
                'tuman',
                'soha']

        for key in keys:
            self.key=None

@bot.message_handler(commands=['help', 'start',] )
def home(message):
        markup = types.InlineKeyboardMarkup()
        itembtn1=types.InlineKeyboardButton (text="🇺🇿Uzbek",callback_data="uz")
        
        itembtn2=types.InlineKeyboardButton(text="🇷🇺Русский",callback_data="ru")
        markup.add(itembtn1,itembtn2)
        msg = bot.send_message(message.chat.id, "🇺🇿O'zingizga kerakli tilni tanlang👇\n\n🇷🇺Выберите нужный язык.👇", reply_markup=markup)
       

       
@bot.callback_query_handler(func = lambda call: True)
def print_all_commands(call):

    if call.data == 'uz':
        
            
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    
                itembtn2=types.KeyboardButton('Registratsiya')
                itembtn1=types.KeyboardButton('Biz haqimizda')
                
    
                markup.add(itembtn2,itembtn1) 
                msg = bot.send_message(call.message.chat.id, 'Kerakli bo'limni tanlang 👇', reply_markup=markup)




                @bot.message_handler(func=lambda message: message.text == 'Biz haqimizda')
                def send_welcome(message):
                    msg = bot.reply_to(message, "https://telegra.ph/IT-PARK-BUXORO-03-29")
                        

                @bot.message_handler(func=lambda message: message.text == "Registratsiya")
                def user_reg(message):
                    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                    itembnt1=types.KeyboardButton('erkak')
                    itembnt2=types.KeyboardButton('ayol')
                    markup.add(itembnt1,itembnt2)
                    msg = bot.send_message(message.chat.id, 'Jinsingizni tanlang:', reply_markup=markup)
                    bot.register_next_step_handler(msg, process_jins_step)
    
    
                def process_jins_step(message):
                    if message.text =='erkak' or message.text=='ayol' :
                        str(message.text)
                        chat_id = message.chat.id
                        user_dict[chat_id] = User(message.text)
        
                        markup = types.ReplyKeyboardRemove(selective=False)

                        msg = bot.send_message(chat_id, "Iltimos ism familiyangizni to'liq kiriting !", reply_markup=markup)
        
                        bot.register_next_step_handler(msg, process_FIO_step)
                    
                    else:
                        msg = bot.reply_to(message, 'Iltimos qaytadan tanlang!' )
                        bot.register_next_step_handler(msg, process_jins_step)



              


                def process_FIO_step(message):
   
                    try :

                        str(message.text)
                        chat_id = message.chat.id
                        user = user_dict[chat_id]
                        user.FIO = message.text
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        itembnt1=types.KeyboardButton('📲 Telefon raqamimni yuborish',request_contact=True)
                        markup.add(itembnt1)
                        msg = bot.send_message(message.chat.id, text="Telegram yoqilgan telefon raqamingizni kontakt ko'rinishida yuboring\n"+
                                                                "Buning uchun  📲Telefon raqamimni yuborish tugmasini bosing", reply_markup=markup)
                        bot.register_next_step_handler(msg, process_phone_step)
                    except Exception as e:
                        msg = bot.reply_to(message, 'Iltimos yoshingizni qaytadan kiriting')
                        bot.register_next_step_handler(msg, process_FIO_step)
 
    



                def process_phone_step(message):
    
                    try:
        
                        chat_id = message.chat.id
                        user = user_dict[chat_id]
                        user.phone = message.contact.phone_number
        
                        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                        itembnt3=types.KeyboardButton('Buxoro sh')
                        itembnt1=types.KeyboardButton('Jondor')
                        itembnt2=types.KeyboardButton('Buxoro')
                        itembnt3=types.KeyboardButton('Buxoro sh')
                        itembnt4=types.KeyboardButton("Qorako'l")
                        itembnt5=types.KeyboardButton('Olot')
                        itembnt6=types.KeyboardButton('Peshku')
                        itembnt7=types.KeyboardButton('Gijduvon')
                        itembnt8=types.KeyboardButton('Romitan')
                        itembnt9=types.KeyboardButton('Vobkent')
                        itembnt10=types.KeyboardButton('Qaravulbozor')
                        itembnt11=types.KeyboardButton('Kogon sh')
                        markup.add(itembnt1,itembnt2,itembnt3,itembnt4,itembnt5,itembnt6,itembnt7,itembnt8,itembnt9,itembnt10,itembnt11)

                        msg = bot.send_message(chat_id,'Siz qaysi shahar/tumandansiz?', reply_markup=markup)
                        bot.register_next_step_handler(msg, process_malumot_step)
                    except Exception as e:
                        msg = bot.reply_to(message, text="Telegram yoqilgan telefon raqamingizni kontakt ko'rinishida yuboring\n"+
                                                    "Buning uchun 📲 Telefon raqamimni yuborish tugmasini bosing.")
                        bot.register_next_step_handler(msg, process_phone_step)



               


                def process_malumot_step(message):
                    try:
                        str(message.text)
                        chat_id = message.chat.id
                        user = user_dict[chat_id]
                        user.tuman = message.text
        
                        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                        itembnt1=types.KeyboardButton('Kompyuter savodxonligi')
                        itembnt2=types.KeyboardButton('Kompyuter grafikasi')
                        itembnt3=types.KeyboardButton('Web-dasturlash')
                        itembnt4=types.KeyboardButton('Robototexnika')
                        itembnt5=types.KeyboardButton('Mobil ilovalar yaratish')
                        markup.add(itembnt1,itembnt2,itembnt3,itembnt4,itembnt5)

                        msg = bot.send_message(chat_id, 'Qaysi kursga bormoqchisiz', reply_markup=markup)
                        bot.register_next_step_handler(msg, process_soha_step)
                    except Exception as e:
                        bot.reply_to(message, 'ooops!!')



                def process_soha_step(message):
                    str(message.text)      
                    chat_id = message.chat.id
                    user = user_dict[chat_id]
                    user.soha = message.text

       
                    bot.send_message(chat_id, getRegData(user, 'tg name', message.from_user.first_name), parse_mode="Markdown")
        
                    bot.send_message('-1001466284053', getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")
                    markup = types.ReplyKeyboardRemove(selective=False)

                    msg = bot.send_message(chat_id, "Tabriklaymiz muvaffaqiyat registratsiyadan o'tingiz.\n Biz tez orada siz bilan bog'lanamiz.\n/start", reply_markup=markup)


    
                def getRegData(user, title, name):
                    t = Template('$title *$name* \n  FIO: *$FIO*\n  Raqam: *$phone* \n Tuman: *$tuman* \n  Tanlagan sohasi: *$soha*')

                    return t.substitute({
                        'title': title,
                        'name': name,
        
                        'FIO':user.FIO,
                        
                        'phone': user.phone,
                        'tuman': user.tuman,
                       
                        'soha': user.soha,
        
                        })
                
    elif call.data=='ru':

                
               


            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    
            itembtn2=types.KeyboardButton('Регистрация')
            itembtn3=types.KeyboardButton('O нас')
    
            markup.add(itembtn2,itembtn3) 
            msg = bot.send_message(call.message.chat.id, 'Выберите нужный раздел 👇', reply_markup=markup)

            @bot.message_handler(func=lambda message: message.text == "O нас")
            def send_welcome(message):
                msg = bot.reply_to(message, 'https://telegra.ph/IT-PARK-BUHARA-03-29' )

#reg/

            @bot.message_handler(func=lambda message: message.text == "Регистрация")
            def user_reg(message):
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                itembnt1=types.KeyboardButton('Мужской')
                itembnt2=types.KeyboardButton('Женский')
                markup.add(itembnt1,itembnt2)
                msg = bot.send_message(message.chat.id, 'Ваш пол?', reply_markup=markup)
                bot.register_next_step_handler(msg, process_jins_step)
    
    
            def process_jins_step(message):
                try:
                    str(message.text)
                    chat_id = message.chat.id
                    user_dict[chat_id] = User(message.text)
        
                    markup = types.ReplyKeyboardRemove(selective=False)

                    msg = bot.send_message(chat_id, "Пожалуйста введите свое полное имя!", reply_markup=markup)
        
                    bot.register_next_step_handler(msg, process_FIO_step)
                except Exception as e:
                    bot.reply_to(message, 'ooops!!')



          

            def process_FIO_step(message):
   
                try:
                    str(message.text)
                    chat_id = message.chat.id
                    user = user_dict[chat_id]
                    user.FIO = message.text
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    itembnt1=types.KeyboardButton('📲 Отправить мой контакт',request_contact=True)
                    markup.add(itembnt1)
                    msg = bot.send_message(message.chat.id, 'Отправьте свой номер в виде контакта\n\n'+
                                                            'Для этого нажмите на кнопку 📲 Отправить мой контакт', reply_markup=markup)
                    bot.register_next_step_handler(msg, process_phone_step)
                except Exception as e:
                    msg = bot.reply_to(message, 'Пожалуйста, введите свой возраст правильно')
                    bot.register_next_step_handler(msg, process_FIO_step)



            def process_phone_step(message):
    
                try:
        
                    chat_id = message.chat.id
                    user = user_dict[chat_id]
                    user.phone = message.contact.phone_number
        
                    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                    itembnt3=types.KeyboardButton('г.Бухоро ')
                    itembnt1=types.KeyboardButton('Жондор р-н')
                    itembnt2=types.KeyboardButton('Бухоро р-н')
                    
                    itembnt4=types.KeyboardButton("Каракульр-н ")
                    itembnt5=types.KeyboardButton('Олот р-н')
                    itembnt6=types.KeyboardButton('Пешку р-н')
                    itembnt7=types.KeyboardButton('Гиждувон р-н')
                    itembnt8=types.KeyboardButton('Ромитан р-н')
                    itembnt9=types.KeyboardButton('Вобкент р-н')
                    itembnt10=types.KeyboardButton('Қаравулбозор р-н')
                    itembnt11=types.KeyboardButton('г.Когон')
                    markup.add(itembnt1,itembnt2,itembnt3,itembnt4,itembnt5,itembnt6,itembnt7,itembnt8,itembnt9,itembnt10,itembnt11)

                    msg = bot.send_message(chat_id, 'Выберите район', reply_markup=markup)
                    bot.register_next_step_handler(msg, process_malumot_step)
                except Exception as e:
                    msg = bot.reply_to(message, 'Отправьте свой номер в виде контакта\n\n'+
                                                'Для этого нажмите на кнопку 📲 Отправить мой контакт')
                    bot.register_next_step_handler(msg, process_phone_step)




            def process_malumot_step(message):
                try:
                    str(message.text)
                    chat_id = message.chat.id
                    user = user_dict[chat_id]
                    user.tuman = message.text
        
                    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                    itembnt1 = types.KeyboardButton ('Компьютер/грамотность')
                    itembnt2 = types.KeyboardButton ('Компьютер/графика')
                    itembnt3 = types.KeyboardButton ('Веб-программирование')
                    itembnt4 = types.KeyboardButton ('Робототехника')
                    itembnt5 = types.KeyboardButton ('Создать мобильные приложения')
                    markup.add(itembnt1,itembnt2,itembnt3,itembnt4,itembnt5)

                    msg = bot.send_message(chat_id, 'Какой курс вы хотите выбрать?', reply_markup=markup)
                    bot.register_next_step_handler(msg, process_soha_step)
                except Exception as e:
                    bot.reply_to(message, 'ooops!!')



            def process_soha_step(message):
                str(message.text)
                chat_id = message.chat.id
                user = user_dict[chat_id]
                user.soha = message.text

       
                bot.send_message(chat_id, getRegData(user, 'tg name', message.from_user.first_name), parse_mode="Markdown")
        
                bot.send_message('-1001466284053', getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")
                markup = types.ReplyKeyboardRemove(selective=False)

                msg = bot.send_message(chat_id, "Поздравляем с успешной регистрацией. \n Мы свяжемся с вами в ближайшее время.\n/start", reply_markup=markup)

                
    
            def getRegData(user, title, name):
                t = Template('$title *$name* \n  ФИО: *$FIO*\n телефонный номер: *$phone* \n округ: *$tuman* \n  выбранное направление: *$soha*')

                return t.substitute({
                    'title': title,
                    'name': name,
        
                    'FIO':user.FIO,
    
                    'phone': user.phone,
                    'tuman': user.tuman,
                    'soha': user.soha,
        
                    })
            @bot.message_handler(content_types=["text"])
            def send_help_text(message):
        
                    markup = types.InlineKeyboardMarkup()
                    itembtn1=types.InlineKeyboardButton (text="🇺🇿Uzbek",callback_data="uz")
        
                    itembtn2=types.InlineKeyboardButton(text="🇷🇺Русский",callback_data="ru")
                    markup.add(itembtn1,itembtn2)
                    msg = bot.send_message(message.chat.id, "🇺🇿O'zingizga kerakli tilni tanlang👇\n\n🇷🇺Выберите нужный язык.👇", reply_markup=markup)
       


       
            @bot.message_handler(content_types=["photo"])
            def send_help_text(message):
                    bot.send_message(message.chat.id, 'Itimos yozing!!!\nПожалуйста напиши!!!')

                
            @bot.message_handler(content_types=["video"])
            def send_help_text(message):
                    bot.send_message(message.chat.id, 'Itimos yozing!!!\nПожалуйста напиши!!!')


                
            @bot.message_handler(content_types=["audio"])
            def send_help_text(message):
                bot.send_message(message.chat.id, 'Itimos yozing!!!\nПожалуйста напиши!!!')
  
                
            @bot.message_handler(content_types=['sticker'])
            def send_help_text(message):
                bot.send_message(message.chat.id, 'Itimos yozing!!!\nПожалуйста напиши!!!')

        

if __name__ == '__main__':
    bot.polling(none_stop=True)

