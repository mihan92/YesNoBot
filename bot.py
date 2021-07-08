import telebot
import random
from key import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Это оцифрованная версия всем известного шара предсказаний. Задай мне вопрос :)".format(message.from_user))

@bot.message_handler(content_types=['text'])
def check(message):
    num = random.randint(0, 1)
    if '?' in message.text:
        if num == 1:
            bot.send_message(message.chat.id, 'Да')
        else:
            bot.send_message(message.chat.id, 'Нет')
    else:
        bot.send_message(message.chat.id, 'Ты не задал вопрос')

bot.polling()