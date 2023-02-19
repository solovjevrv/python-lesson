# Задача 2. Добавьте в бота игру «Угадай числа».
# Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
from telebot import types
from api_key import API_TOKEN
from random import randint

game_started = False
bot_number = None
counter_step = 0
TOKEN = API_TOKEN
bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=3)
game_btn = types.KeyboardButton("играть")
markup.add(game_btn)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Введите команду 'play' и начните игру.", reply_markup=markup)


@bot.message_handler(content_types="text")
def read_text_message(message):
	global game_started
	global bot_number
	global counter_step
	if game_started:
		if message.text.isdigit():
			number = int(message.text)
			if number > bot_number:
				bot.reply_to(message, f"Я загадал число меньше, чем {number}")
				counter_step += 1
			elif number < bot_number:
				bot.reply_to(message, f"Я загадал число больше, чем {number}")
				counter_step += 1
			elif number == bot_number:
				game_started = False
				bot.reply_to(message, f"Верно! Ты угадал c {counter_step} попыток! Я загадал число {bot_number}")
			else: bot.reply_to(message, "Ничего не понял...")
		else: 
			bot.reply_to(message, "Я ожидал число...")
	if message.text == "играть":
		if not game_started:
			game_started = True
			bot_number = randint(1, 100)
			print(bot_number)
			bot.reply_to(message, "Бот загадал число от 1 до 100. Ваша задача отгадать его.")
		else: 
			bot.reply_to(message, "Игра уже началась")
	


bot.infinity_polling()
