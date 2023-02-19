
from random import randint

bot_number = randint(1, 10)


def game(bot_number):
    print(bot_number)
    counter_step = 0
    result = ""
    while True:
        user_number = int(
            input("Введите загаданное ботом число: "))
        counter_step += 1
        if bot_number == user_number:
            result = f"Вы угадали с {counter_step} попытки(ок). Бот загадал число {bot_number}."
            break
    return result


# print(game(bot_number))

# return f"Вы угадали с {counter_step} попытки(ок). Бот загадал число {bot_number}."
