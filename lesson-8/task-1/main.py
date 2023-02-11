# Задача 1. В каждой группе учится от 20 до 30 студентов.
# По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
import random
group_count = 4

marks = [0] * group_count

for i in range(group_count):
    marks[i] = [random.randint(2, 5) for _ in range(random.randint(20, 30))]

for row in marks:
    print(row)

mark_max = 0
group_max = 0

for i in range(group_count):
    average_max = 0
    student_count = len(marks[i])
    for j in range(student_count):
        average_max += marks[i][j]
    average_max /= student_count
    # print(average_max)
    if average_max > mark_max:
        mark_max = average_max
        group_max = i + 1

print(
    f"Максимальный средний балл у группы: {group_max}")
