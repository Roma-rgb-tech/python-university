names = []
grades = []

n = int(input("Введіть кількість студентів: "))

for i in range(n):
    name = input("Введіть ім'я: ")
    names.append(name)

    try:
        grade = float(input("Введіть оцінку: "))
    except:
        print("Помилка! Ставлю 0")
        grade = 0

    grades.append(grade)

s = 0
for g in grades:
    s = s + g

avg = s / n
print(f"Середній бал = {avg}")


print("Студенти нижче середнього:")
for i in range(n):
    if grades[i] < avg:
        print(names[i], grades[i])
        
        