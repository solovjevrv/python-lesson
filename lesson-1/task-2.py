# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math

def distance(x1, y1, x2, y2):
    Distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return Distance

print("Введите координаты точки A (x, y):")
x1 = int(input()) 
y1 = int(input()) 
print("Введите координаты точки B (x, y):")
x2 = int(input()) 
y2 = int(input())
print("Расстояние между точками:")
print(distance(x1, x2, y1, y2))
