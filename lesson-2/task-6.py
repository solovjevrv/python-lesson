# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
X= 0
Y= 0
Z = 0
def table(X, Y, Z):
    print("X Y Z ¬(X ∧ Y) ∨ Z")
    print("-------------------")
    for x in [True, False]:
      for y in [True, False]:
        for z in [True, False]:
            print(x, y, z, (not(x and y) or z))

table(X, Y, Z)