# 1 Задание 
def dec(saske):
    count = 0
    def c(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция {saske.__name__}",f"вызовов {count} раз")
        return saske(*args, **kwargs)
    return c

@dec
def hello(x):
    print("HELLO!")
    print("Привет" " " f"{x}")

hello("Илья")

# 2 Задание 

# def fib():
#     x = 0
#     y = 1 
#     while True:
#         p = x + y
#         x = y
#         y = p
#         yield x
# for i in fib():
#     print(i)

# 3 Задание 

def quick_sort(n):
    if len(n) <= 1:
        return n 
    c = n[len(n) // 2]
    l = [i for i in n if i < c]
    t = [i for i in n if i == c]
    r = [i for i in n if i > c]
    return quick_sort(l) + t + quick_sort(r)

m = [1,2,3,4,6,7,4,0]
print(quick_sort(m))

