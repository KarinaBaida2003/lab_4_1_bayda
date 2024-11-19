def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Приклад використання:
n = int(input("Введіть число n: "))
print(f"Факторіал {n}! = {factorial_recursive(n)}")
