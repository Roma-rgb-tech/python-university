# Практична робота №1 

# Частина 1: Введення даних та підготовка до розрахунку вартості 
from datetime import datetime 

initial_price = 20000

year_of_manufacture = int(input("Введіть рік випуску автомобіля: "))
current_mileage = int(input("Введіть пробіг автомобіля(у км): "))

current_year = datetime.now().year

# Частина 2: Розрахунок вартості та середньорічного пробігу
age_of_car = current_year - year_of_manufacture
depreciation = age_of_car * 0.1
final_price = initial_price * (1 - depreciation)

if age_of_car > 0:
    average_annual_mileage = current_mileage / age_of_car
else:
    average_annual_mileage = current_mileage
    
# Частина 3: Виведення результату 
print(f"Інформація про автомобіль: ")
print(f"- Рік випуску:{year_of_manufacture} років")
print(f"- Первісна вартість: {initial_price} грн")
print(f"- Пробіг автомобіля: {current_mileage} км")
print(f"- Середній річний пробіг: {average_annual_mileage:.0f} км/рік")
print(f"- Орієнтовна поточна вартість: {final_price:.2f} грн")

# Частина 3: Виведення результату 
print(f""" 
Інформація про автомобіль:
- Рік випуску: {year_of_manufacture}
- Вік автомобіля: {age_of_car} років
- Первісна вартість: {initial_price} грн
- Пробіг автомобіля: {current_mileage} км
- Середній річний пробіг: {average_annual_mileage:.0f} км/рік
- Орієнтовна поточна вартість: {final_price:.2f} грн""")