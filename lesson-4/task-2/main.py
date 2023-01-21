# Задача 2. В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»



def getProductOutStock():
    file = open("icecream.txt", mode='r', encoding="utf=8")
    data = file.readlines()
    productAll = set(data[0].split(", "))
    productInStock = set(data[1].split(", "))
    productOutStock = productAll.difference(productInStock)
    print(f"Закончилось: {str(productOutStock)}")

getProductOutStock()
