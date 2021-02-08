import telebot
from telebot import types
from string import Template
bot=telebot.TeleBot('1648785365:AAE3i1nDRp9xjBtDkCrl9S2OmAoiCSZH_MI')
user_dict = {}

class User:
    def __init__(self,city):
        self.city=city

        keys = ['jins','FIO','yosh','phone',
                'tuman','manzil','malumot',
                'soha']

        for key in keys:
            self.key=None

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    
    itembtn2=types.KeyboardButton('/Registratsiya')
    itembtn3=types.KeyboardButton('/Manzil')
    
    markup.add(itembtn2,itembtn3) 
    msg = bot.reply_to(message, 'Assalamu aleykum '+ message.from_user.first_name+'\n Jondor IT CENTERning rasmiy botiga xush kelibsiz', reply_markup=markup)






@bot.message_handler(commands=['Manzil'])
def send_welcome(message):
    msg = bot.reply_to(message, "Buxoro shahar, Jomiy ko'chasi, 1 uy (xarita) (https://yandex.com/maps/-/CCUIMOuw2C). Mas'ul xodim: Bo'ratov Baxtiyor. Telefon: +998 93 685-50-97\n "
                                +"Buxoro tumani, Buxoro shossesi, 5 uy (xarita) (https://yandex.uz/maps/-/CCUIJRaC3B). Mas'ul xodim: Saidov Abdurahmon. Telefon: +998 91 406-63-39\n"
                                +"Kogon shahar, Buxoro shossesi, 12 uy (xarita) (https://yandex.uz/maps/-/CCQ~YKaywA). Mas'ul xodim: Qayumov Shahriyor. Telefon: +998 93 681-06-18\n"
                                +"Olot tumani, Olot ko'chasi, 71 uy (xarita) (https://yandex.uz/maps/-/CCQ~YKegkC). Mas'ul xodim: Rustamov Jo'shqin. Telefon: +998 94 120-69-66\n"
                                +"Qorako'l tumani, Ulug'bek ko'chasi, 32 uy (xarita) (https://yandex.uz/maps/-/CCQ~YKqwPB). Mas'ul xodim: Abdullayev Og'abek. Telefon: +998 99 700-08-98\n"
                                +"Jondor tumani, Istiqlol ko'chasi, 1 uy (xarita) (https://yandex.com/maps/-/CCUIMCUr9A). Mas'ul xodim: Rayimberdiyev Dilshod. Telefon: +998 99 705-91-24\n"
                                +" G'ijduvon tumani, XXI-asr ko'chasi, 5 uy (xarita) (https://yandex.com/maps/-/CCUIJRVicB). Mas'ul xodim: Rajabov Umarjon. Telefon: +998 90 329-92-95\n"
                                +"Romitan - Romitan tumani,Baxoriston ko'chasi , 72-uy.\n"
                                +"QorovulBozor - Qorovulbozor tuman,Geologlar ko'chasi , 15-uy, 1-qavat\n"
                                +"Shofirkon - Shofirkon tumani,Mustaqillik ko'chasi , 5-uy\n"
                                +"Peshku - Peshku tumani, O'zbekiston ko'chasi , 31-uy, 1-qavat"
                                )

#reg/

@bot.message_handler(commands=['Registratsiya'])
def user_reg(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembnt1=types.KeyboardButton('erkak')
    itembnt2=types.KeyboardButton('ayol')
    markup.add(itembnt1,itembnt2)
    msg = bot.send_message(message.chat.id, 'Jinsingiz', reply_markup=markup)
    bot.register_next_step_handler(msg, process_jins_step)
    
    
def process_jins_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, "Iltimos ism familiyangizni to'liq kiriting !", reply_markup=markup)
        
        bot.register_next_step_handler(msg, process_FIO_step)
    except Exception as e:
       bot.reply_to(message, 'ooops!!')



def process_FIO_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.FIO = message.text
        
        msg = bot.send_message(chat_id, 'Yosh kiriting')
        bot.register_next_step_handler(msg, process_yosh_step)

    except Exception as e:
       bot.reply_to(message, 'ooops!!')



def process_yosh_step(message):
   
        

    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.yosh = message.text
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    itembnt1=types.KeyboardButton('Raqamingizni yuboring',request_contact=True)
    markup.add(itembnt1)
    msg = bot.send_message(message.chat.id, 'Raqamingizni yuboring', reply_markup=markup)
    bot.register_next_step_handler(msg, process_phone_step)

    



def process_phone_step(message):
    
    try:
        
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.contact.phone_number
        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembnt1=types.KeyboardButton('Jondor')
        itembnt2=types.KeyboardButton('Buxoro')
        itembnt3=types.KeyboardButton('Buxoro sh')
        itembnt4=types.KeyboardButton("Qorako'l")
        itembnt5=types.KeyboardButton('Olot')
        itembnt6=types.KeyboardButton('Peshku')
        itembnt7=types.KeyboardButton('Gijduvon')
        itembnt8=types.KeyboardButton('Rominat')
        itembnt9=types.KeyboardButton('Vobkent')
        itembnt10=types.KeyboardButton('Qaravulbozor')
        itembnt11=types.KeyboardButton('Kogon sh')
        markup.add(itembnt1,itembnt2,itembnt3,itembnt4,itembnt5,itembnt6,itembnt7,itembnt8,itembnt9,itembnt10,itembnt11)

        msg = bot.send_message(chat_id, 'Tumanini tanlang', reply_markup=markup)
        bot.register_next_step_handler(msg, process_Tuman_step)
    except Exception as e:
        msg = bot.reply_to(message, 'Iltimos raqamingizni yuboring')
        bot.register_next_step_handler(msg, process_phone_step)



def process_Tuman_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.tuman = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(message.chat.id, 'Yashash manzilini kiriting ', reply_markup=markup)
    
        
        bot.register_next_step_handler(msg, process_manzil_step)

    except Exception as e:
       bot.reply_to(message, 'ooops!!')




def process_manzil_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.manzil = message.text
        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembnt1=types.KeyboardButton("O'quvchi")
        itembnt2=types.KeyboardButton('Talaba')
        itembnt3=types.KeyboardButton('Ishchi')
        itembnt4=types.KeyboardButton('Ishsiz')
        itembnt5=types.KeyboardButton('Nafaqada')
        markup.add(itembnt1,itembnt2,itembnt3,itembnt4,itembnt5)

        msg = bot.send_message(chat_id, "Ma'lumotingiz qanday??", reply_markup=markup)
        bot.register_next_step_handler(msg, process_malumot_step)
    except Exception as e:
        bot.reply_to(message, 'ooops!!')




def process_malumot_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.malumot = message.text
        
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
    
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.soha = message.text

       
    bot.send_message(chat_id, getRegData(user, 'tg name', message.from_user.first_name), parse_mode="Markdown")
        
    bot.send_message('-599517312', getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")
    markup = types.ReplyKeyboardRemove(selective=False)

    msg = bot.send_message(chat_id, "Tabriklaymiz muvaffaqiyat registratsiyadan o'tingiz.\n Biz tez orada siz bilan bog'lanamiz\nRegistartsiya - /Registartiya\nYordam - /help", reply_markup=markup)


    
def getRegData(user, title, name):
    t = Template('$title *$name* \n  FIO: *$FIO*\n Yosh: *$yosh* \n Raqam: *$phone* \n tuman: *$tuman* \n Yashash manzil: *$manzil* \n Malumoti: *$malumot* \n Tanlagan sohasi: *$soha*')

    return t.substitute({
        'title': title,
        'name': name,
        
        'FIO':user.FIO,
        'yosh': user.yosh,
        'phone': user.phone,
        'tuman': user.tuman,
        'manzil': user.manzil,
        'malumot': user.malumot,
        'soha': user.soha,
        
    })





@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'Registartsiya - /Registratsiya\nYordam - /help')




@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Itimos yozing')



bot.polling(none_stop=True)
    