# Напишите бота для техподдержки.
# Бот должен записывать обращения пользователей в файл.

import telebot
from api_key import API_TOKEN
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Здравствуйте! Я Бот техподдержки. Введите команду /support, чтобы оставить свой вопрос.")


@bot.message_handler(commands=['support'])
def support(message):
    bot.reply_to(
        message, "Напишите свой вопрос в одном сообщении.")
    bot.register_next_step_handler(message, write_question)


def write_question(message):
    data = open("question.txt", mode="a", encoding="utf-8")
    data.write(
        f"{message.from_user.id}|{message.from_user.first_name} {message.from_user.last_name}|{message.text} \n")
    data.close()
    bot.reply_to(message, "Ваш вопрос отправлен в службу техничческой поддержки. Среднее время ожидания ответа 5 минут.")


bot.infinity_polling()
