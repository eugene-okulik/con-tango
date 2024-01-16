def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b



fibo = fibonacci_generator()



def fibo_number(n):
    for _ in range(n - 1):
        next(fibo)
    return next(fibo)



print(f"Пятое число: {fibo_number(5)}\n")
print(f"Двухсотое число: {fibo_number(200)}\n")
print(f"Тысячное число: {fibo_number(1000)}\n")
print(f"Стотысячное число (лучше его не видеть;): {fibo_number(100000)}")
