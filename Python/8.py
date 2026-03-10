import math

def run_greeting():
    # КРОК 9: Персональне вітання (об'єднана функція)
    print("--- Реєстрація користувача ---")
    name = input("Введіть ваше ім'я: ").strip().title()
    surname = input("Введіть ваше прізвище: ").strip().title()
    print("\n" + "="*40)
    print(f"Вітаємо у системі, {name} {surname}!")
    print("Програма готова до виконання математичних розрахунків.")
    print("="*40 + "\n")

def print_menu():
    # КРОК 1: Головне меню
    print("\n--- ГОЛОВНЕ МЕНЮ ---")
    print("1. Координати точки (2D, 3D)")
    print("2. Обчислення математичних виразів")
    print("3. Периметр трикутника")
    print("4. Робота з колом ")
    print("5. Рівняння лінії ")
    print("6. Форматування чисел")
    print("7. Виведеня рівняння ")
    print("8. Вихід")
    print("--------------------")

def handle_coordinates():
    # КРОК 2: Робота з координатами
    choice = input("Оберіть тип (2D/3D): ").strip().lower()
    try:
        x = float(input("Введіть x: "))
        y = float(input("Введіть y: "))
        if choice == "3d":
            z = float(input("Введіть z: "))
            print(f"Результат: Точка P({x:.2f}, {y:.2f}, {z:.2f})")
        else:
            print(f"Результат: Точка P({x:.2f}, {y:.2f})")
    except ValueError:
        print("Помилка: введіть числові значення!")

def calculate_expressions():
    # КРОК 3: Обчислення математичних виразів
    try:
        a = float(input("Введіть a: "))
        b = float(input("Введіть b: "))
        

        res1 = math.sin(a) + math.cos(b)

        res2 = math.log(a**2 + 1)
        
        print(f"Результати:")
        print(f"1. sin({a}) + cos({b}) = {res1:.4f}")
        print(f"2. ln({a} + 1) = {res2:.4f}")
    except ValueError:
        print("Помилка: некоректні дані.")

def triangle_perimeter():
    # КРОК 4: Периметр трикутника
    try:
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))
        
        if a + b > c and a + c > b and b + c > a:
            p = a + b + c
            print(f"Периметр трикутника: P = {p:.2f}")
        else:
            print("Помилка: трикутник з такими сторонами не існує.")
    except ValueError:
        print("Помилка: введіть числа.")
        
def line_equation():
    # КРОК 5: Використання функцій модуля math
    try:
        print("Введіть координати двох точок:")
        x1, y1 = float(input("x1: ")), float(input("y1: "))
        x2, y2 = float(input("x2: ")), float(input("y2: "))
        
        if x1 == x2:
            print(f"Рівняння вертикальної лінії: x = {x1}")
        else:
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            sign = "+" if b >= 0 else "-"
            print(f"Рівняння лінії: y = {k:.2f}x {sign} {abs(b):.2f}")
    except ValueError:
        print("Помилка введення.")

def circle_operations():
    # КРОК 6: Робота з колом
    try:
        l = float(input("Введіть довжину кола (L): "))
        if l > 2:
            radius = l / (2 * math.pi)
            area = math.pi * radius**2
            print(f"Радіус (r): {radius:.4f}")
            print(f"Площа круга (S): {area:.4f}")
        else:
            print("Довжина повинна бути більше 0.")
    except ValueError:
        print("Помилка введення.")

def formater_num():
    # Крок 7: Форматування чисел
    try:
        number = float(input("Введіть число: "))
        precision = int(input("Введіть кількість знаків після коми: "))
        
        print(f"\nРезультати форматування для {number}:")
        
        print(f"-> Фіксована точка (f): {number:.{precision}f}")
        print(f"-> Науковий формат (e): {number:.{precision}e}")
        
    except ValueError:
        print("Помилка: введіть числові значення (точність має бути цілим числом).")
        
def linear_eq_view():
    # Крок 8: Виведення рівняння 
    try:
        a = float(input("Введіть a: "))
        b = float(input("Введіть b: "))
        sign = '+' if b >= 0 else "-"
        print(f"Рівняння: {a}x {sign} {abs(b)} = 0")
    except ValueError:
        print("Помилка.")

def main():
    run_greeting() 
    while True:
        print_menu()
        choice = input("Ваш вибір(1-8): ")
        
        if choice == '1':
            handle_coordinates()
        elif choice == '2':
            calculate_expressions()
        elif choice == '3':
            triangle_perimeter()
        elif choice == '4':
            circle_operations()
        elif choice == '5':
            line_equation()
        elif choice == '6':
            formater_num()
        elif choice == '7':
            linear_eq_view()
        elif choice == "8":
            print("Програма завершена. До побачення!")
            break
        else:
            print("Невірний пункт меню, спробуйте ще раз.")

if __name__ == "__main__":
    main()
    
