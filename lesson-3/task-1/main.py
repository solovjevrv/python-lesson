# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

n = int(input("Введите сколько числе Фиббоначи вы хотите сохранить: "))

f1, f2 = 1, 1
fibbonaci = ""

for i in range(n):
    fibbonaci += str(f1) + " "
    f1, f2 = f2, f1 + f2

file = open("fibbonaci.txt", "w+")
file.write(fibbonaci)
print(f"Последовательность Фиббоначи вида: {fibbonaci} успешно записано в файл fibbonaci.txt")
file.close()
