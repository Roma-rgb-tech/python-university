# a)
def F(a):
    a += 1
    return a

def g(x):
    x = 2
    return x

a = 3
b = 44
print(F(a), g(b), a, b) # 4, 2, 3, 44


# б)
def f1(x, y):
    z = x + y
    x += 1
    y -= 1
    tmp = f2(z, x, y)
    print(x, y, z) # 2, -1, 1
    return tmp

def f2(x, y, z):
    tmp = x + y + z
    x = y = z = 0
    return tmp

x = 0
y = 1
z = 2
res = f1(y, x)
print(x, y, z, res) #  0, 1, 2, 2

# в)
def f1(x, y, z):
    x -= 1
    y += 1
    z += 2
    print(x, y, z) # -1, 2, 4
    tmp = f2(x, y, z)
    print(x, y, z) # 2, 4, 4
    return tmp

def f2(x, y, z):
    x, y, x = x, z, y
    print(x, y, z) # -1, 2, 4
    return x + y + z

x = 0
y = 1
z = 2
res = f1(x, y, z)
print(x, y, z, res) # 0, 1, 2, 10






#2.Указати помилки, наявні в коді.

# a)
def f1(a, b, c=3): pass
f1(1, b=1, c=3)
f1(1, c=1, c=3) # Помилка
f1(1, b=1)
f1(1, 2, b=1) # Помилка
f1(b=1) # Помилка
f1(b=1, 1) # Помилка
f1(b=1, a=1)
f1(c=5, b=1, a=1)

# б)
def f2(a, /, b, *, c=3, d=4): pass 
f2(4, d=5) # Помилка
f2(a=4, 3, d=5) # Помилка
f2(4, 3, d=5)
f2(4, b=3, d=5)
f2(1, 2)
f2(1, 2, 4) # Помилка
f2(1, 2, d=4, c=5)