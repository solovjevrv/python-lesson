# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть ли в массиве последовательность 
# из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
from random import randint

num = int(input("Введите трехзначное наруральное число, например 123: "))

def getRandomArray():
  array = []
  for _ in range(15):
    array.append(randint(1, 10))
  return array

def findNumInArray(num, array):
  counter = 0
  s = ""
  for i in range(len(array)):
      s += str(array[i])
  for i in range(int(len(s)/3)):
      if(s[:3] == str(num)):
        counter += 1
      s = s.replace(s[:3], "")
  if(counter >= 1): return True
  else: return False

print(getRandomArray())
print(findNumInArray(num, getRandomArray()))