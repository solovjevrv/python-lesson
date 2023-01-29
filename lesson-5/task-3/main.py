# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаю. Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

from random import randint
numbers = []
dictionary2 = {}
counter = 0
for i in range(10):
    numbers.append(randint(1, 10))
print(f"Исходный массив:{numbers}")
for i in range(len(numbers)):
    if(dictionary2.get(numbers[i])):
        dictionary2[numbers[i]] += 1
        counter += 1
    else: dictionary2[numbers[i]] = 1

print(f"Массив без повторяющихся элементов: {list(dictionary2.keys())}")
print(f"Количество повторяющихся элементов: {counter}")

