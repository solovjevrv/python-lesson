# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396

N = int(input("Введите число N: "))

def getResult(N):
    NN = int(str(N)+str(N))
    NNN = int(str(N)+str(N) + str(N))
    SUM = N + NN + NNN
    return SUM

print(getResult(N))