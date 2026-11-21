# Вариант: 1

# Задание: 2

a = list(map(int, input("Введи вектор:").split()))
b = list(map(int, input("Введи вектор:").split()))
c = 0
for x,y in zip(a,b):
    c =+ x * y
print(c)

# zip - команда, котора объединяет элементы двух списков в пары

# Задание: 3

x = input()
def ss(x):
    c = 0
    for i in x:
        c = c * 2 + int(i)
    return c
print(ss(x))