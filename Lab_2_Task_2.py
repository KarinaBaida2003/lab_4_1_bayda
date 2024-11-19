def binary_search(array, x):
    """
    Бінарний пошук у відсортованому масиві.
    :param array: Відсортований список елементів
    :param x: Шуканий елемент
    :return: Індекс першого входження елемента або -1, якщо елемент відсутній
    """
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Середній індекс
        
        if array[mid] == x:
            # Ми знайшли елемент, але треба знайти перше входження
            # Рухаємося ліворуч, щоб знайти перший елемент
            while mid > 0 and array[mid - 1] == x:
                mid -= 1
            return mid
        
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # Якщо елемент не знайдено
a = [1, 4, 4, 4, 4, 12, 14]

assert binary_search(a, 4) == 1
assert binary_search(a, 1) == 0
assert binary_search(a, 10) == -1

print("Усі тести пройдено успішно!")
