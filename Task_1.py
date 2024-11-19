
def last_digit_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10
    
    return current

# Приклад використання:
n = int(input("Введіть n: "))
print("Остання цифра", n, "-го числа Фібоначчі:", last_digit_fibonacci(n))

