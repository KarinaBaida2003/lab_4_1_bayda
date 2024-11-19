def merge_sort(array):
    """
    Алгоритм сортування злиттям
    :param array: Масив для сортування
    :return: Відсортований масив
    """
    if len(array) <= 1:
        return array
    
    # Розділяємо масив на дві частини
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    
    # Зливаємо дві відсортовані частини
    return merge(left_half, right_half)

def merge(left, right):
    """
    Зливає два відсортованих масиви в один
    :param left: Ліва частина
    :param right: Права частина
    :return: Відсортований масив
    """
    sorted_array = []
    i = j = 0
    
    # Зливаємо два масиви
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Додаємо залишки
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array
import random
import time

# Реалізація сортування злиттям
def merge_sort(array):
    """
    Алгоритм сортування злиттям
    :param array: Масив для сортування
    :return: Відсортований масив
    """
    if len(array) <= 1:
        return array
    
    # Розділяємо масив на дві частини
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    
    # Зливаємо дві відсортовані частини
    return merge(left_half, right_half)

def merge(left, right):
    """
    Зливає два відсортованих масиви в один
    :param left: Ліва частина
    :param right: Права частина
    :return: Відсортований масив
    """
    sorted_array = []
    i = j = 0
    
    # Зливаємо два масиви
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Додаємо залишки
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Функція для перевірки результату сортування
def checkResult(array):
    """ Перевіряє впорядкованість масиву даних за зростанням
    :param array: масив
    """
    errors = 0
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            errors += 1

    print("Errors:       ", errors)

# Функція для тестування сортування
def testSort(method='merge'):
    assert method in ['merge']

    # Генеруємо випадковий масив
    s = [random.randint(-100000, 100000) for _ in range(N)]
    
    # Запускаємо сортування
    t = time.process_time()
    if method == 'merge':
        s = merge_sort(s)
    dt = time.process_time() - t
    
    print('Sorting time: ', dt)
    checkResult(s)

# Налаштування розміру масиву
N = 1000000

# Тестуємо сортування злиттям
testSort(method="merge")
