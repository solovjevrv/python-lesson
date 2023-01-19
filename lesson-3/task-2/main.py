# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

file = open("fruits.txt", encoding="utf-8", mode="r")
fruits = file.read().splitlines()

fruits_for_print = []
letter = str(input("Введите букву? "))

for i in range(len(fruits)):
    if(letter.lower() == fruits[i][0].lower()):
        fruits_for_print.append(fruits[i])
if (fruits_for_print != []):
    for i in range(len(fruits_for_print)):
        print(fruits_for_print[i])
else: print(f"Фрутов на букву {letter} не найдено!")


