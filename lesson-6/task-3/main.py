# Задача 3. Найдите все простые несократимые дроби, 
# лежащие между 0 и 1, знаменатель которых не превышает 11.

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

results = []
for denominator in range(1, 12):
    for numerator in range(1, denominator + 1):
        if numerator / denominator < 1 and gcd(numerator, denominator) == 1:
            results.append(numerator / denominator)
print(results)