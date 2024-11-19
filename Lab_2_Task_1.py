def modified_linear_search(array, x):
    """
    Лінійний пошук останнього входження елемента в масиві
    :param array: Список елементів
    :param x: Шуканий елемент
    :return: Індекс останнього входження, або -1, якщо елемент відсутній
    """
    last_index = -1  # Змінна для зберігання індексу останнього входження
    for i in range(len(array)):
        if array[i] == x:
            last_index = i  # Оновлюємо індекс при кожному збігу
    return last_index  # Якщо last_index не змінився, повертає -1
a = [2, 2, 2, 4, 4, 5, 8, 3, 1, 10, 54]

# Тестування
assert modified_linear_search(a, 2) == 2
assert modified_linear_search(a, 4) == 4
assert modified_linear_search(a, 12) == -1

print("Усі тести пройдено!")
