import telebot
from api_key import API_TOKEN
bot = telebot.TeleBot(API_TOKEN)


def send_answer(id, question, answer):
    bot.send_message(id, f"{question}\n Ответ: {answer}")


data = open("question.txt", mode="r", encoding="utf-8")
question_list = data.readlines()
data.close()

answered_questions = []

for row in question_list:
    split_row = row.split("|")
    id = split_row[0]
    question = split_row[2]
    print(question)
    answer = input("Введите ответ: ")
    if answer != "пропустить":
        send_answer(id, question, answer)
        answered_questions.append(row)
    print("_____________________________")

for answer in answered_questions:
    question_list.remove(answer)

data = open("question.txt", mode="w", encoding="utf-8")
data.writelines(question_list)
data.close()
