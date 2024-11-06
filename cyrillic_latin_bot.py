from transliterate import to_cyrillic, to_latin
import telebot

token = '7927408309:AAF2iyCyTgqrkuxv-nfgjlrqinG0gZZu9IM'
bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    answer = "Hello 👋, I am 🤖 Cyrillic — Latin.Bot\n \nI can convert words written in the Cyrillic alphabet to the Latin alphabet and vice versa 🔁\n"
    answer += "\nEnter text: ⬇️"
    bot.reply_to(message, answer)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    # if msg.isascii():
    #     answer = to_cyrillic(msg)
    # else:
    #     answer = to_latin(msg)
    
    bot.reply_to(message, answer(msg))

bot.infinity_polling()
