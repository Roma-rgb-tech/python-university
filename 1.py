1 
name = input("Ваще прізвище, ім'я, по батькові?: ")
age = input("Скільки вам років?: ")
city = input("Де ви живете?: ")
study_place = input("Де ви навчаєтесь?: ")
group_number = input("Номер вашої групи?: ")
place_number = input("Який ваш порядковий номер у списку групи?: ")

print("Ваше ім'я: ", name)
print("Ваш вік: ", age)
print("Ви живете в ", city)
print("Ви навчаєтесь в ",study_place)
print("Номер моєї групи-", place_number)
print("Мій порядковий номер у списку групи-", place_number)

# 2
import math
x = float(input("Введіть x(останню цифру у списку групи): "))
t = 1

Z = ((9 * math.pi * t + 10 * math.cos(x)) /
     (math.sqrt(t) - abs(math.sin(t)))) * math.exp(x)

print(f"Z = {Z:.2f}")




# 3
import math

x = float(input("Введіть x: "))

if x >= 0:
    f = 0.5 - abs(x) ** 1.4
else:
    f = (math.sinx**2 **2) / abs(x + 1)
    
print(f"f(x) = {f:.2f}")



# 4
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третье число: "))
N = int(input("Введіть N: "))

print("Числа, що належать інтервалу [1, N]: ")

if 1 <= a <= N:
    print(a)
    
if 1 <= b <= N:
    print(b)

if 1 <= c <= N:
    print(c)
    


a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третье число: "))

min_value = min(a, b, c)
max_value = max(a, b, c)

print("Мінімальне серед чисел: ", min_value)
print("Максимальне серед чисел: ", max_value)