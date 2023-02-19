# Задача 1. Добавьте telegram-боту возможность вычислять выражения:1 + 4 * 2 -> 9

import telebot
from api_key import API_TOKEN
TOKEN = API_TOKEN 

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Введите команду 'eval' и после нее выражение, которое вы хотите посчитать\
""")


@bot.message_handler(commands=['eval'])
def evaluate_expression(message):
    expression = message.text.split()[1:]
    expression = ''.join(expression)
    print(expression)
    try:
        result = eval(expression)
        bot.reply_to(message, f"Результат: {result}")
    except:
        bot.reply_to(message, "Введите корректное выражение")


bot.polling()
