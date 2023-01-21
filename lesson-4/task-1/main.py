# Задача 1. Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

import math 

def findSimpleNumbers(num): 
    while num % 2 == 0: 
        print(2,) 
        num = num / 2 
    for i in range(3, int(math.sqrt(num)) + 1, 2): 
        while num % i == 0: 
            print(i,) 
            num = num / i 
    if num > 2: 
        print(int(num)) 

num = int(input("Введите число: "))
findSimpleNumbers(num) 
