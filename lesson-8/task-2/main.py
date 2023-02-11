# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random

def sum_of_rows_exceeding_main_diagonal(n):
    matrix = [[random.randint(1,100) for j in range(n)] for i in range(n)]
    print("Заданная матрица:")
    for row in matrix:
        print(row)

    main_diagonal_sum = sum([matrix[i][i] for i in range(n)])
    print("Сумма элементов в главной диагонали:", main_diagonal_sum)

    row_sums = [sum(matrix[i]) for i in range(n)]
    print("Суммы строк:", row_sums)

    exceeding_rows = [i for i in range(n) if row_sums[i] > main_diagonal_sum]
    print("Наибольшая строка по сумме:", exceeding_rows)

    sum_of_elements = sum([sum(matrix[i]) for i in exceeding_rows])
    print("Сумма элементов в наибольшей строке:", sum_of_elements)

sum_of_rows_exceeding_main_diagonal(3)