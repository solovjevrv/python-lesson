# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца.
# Выведите их даты.
import random


def periods_for_mouth(temp_in_month, period, month):
    max_temp = 0
    day_max_temp = 1
    min_temp = 1000
    day_min_temp = 1

    for day in range(len(temp_in_month) - period + 1):
        temp_in_period = temp_in_month[day:day + period]
        sum_temp_in_period = sum(temp_in_period)
        # print(
        #     f" {day+1} - {day + period}, {temp_in_period}, Ср. тем-ра: {round(sum_temp_in_period/period, 1)}")
        if sum_temp_in_period > max_temp:
            max_temp = sum_temp_in_period
            day_max_temp = day
        elif sum_temp_in_period < min_temp:
            min_temp = sum_temp_in_period
            day_min_temp = day
    print(f"В течении месяца {month} максимальная температура была: {round(max_temp/period, 1)} в период с {day_max_temp+1} по {day_max_temp + period}, а минимальная температура: {round(min_temp/period, 1)} в период с {day_min_temp+1} по {day_min_temp + period}")
    # print(
    #     f"Максимальная температура {round(max_temp/period, 1)} была с {day_max_temp+1} по {day_max_temp + period} {month} ")
    # print(
    #     f"Минимальная температура  {round(min_temp/period, 1)} была с {day_min_temp+1} по {day_min_temp + period} {month} ")


temp_in_month = [random.randint(18, 32) for _ in range(31)]
month_names = ["Май", "Июнь", "Июль", "Август", "Сентябрь"]

for i in range(len(month_names)):
    periods_for_mouth(temp_in_month, 7, month_names[i])
