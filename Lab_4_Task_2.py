import random

def randomize_partition(array, p, r):
    """
    Вибирає випадковий опорний елемент для розбиття масиву.
    :param array: Масив
    :param p: Початкова позиція
    :param r: Кінцева позиція
    :return: Індекс опорного елемента після розбиття
    """
    random_pivot_index = random.randint(p, r)  # Випадковий вибір опорного елемента
    array[r], array[random_pivot_index] = array[random_pivot_index], array[r]  # Обмін з останнім елементом
    return partition(array, p, r)

def partition(array, p, r):
    """
    Стандартна функція розбиття масиву (як у класичному швидкому сортуванні).
    :param array: Масив
    :param p: Початкова позиція
    :param r: Кінцева позиція
    :return: Індекс опорного елемента після розбиття
    """
    pivot = array[r]  # Опорний елемент
    i = p - 1  # Індекс меншого елемента

    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # Обмін елементів

    array[i + 1], array[r] = array[r], array[i + 1]  # Поміщаємо опорний елемент у правильне місце
    return i + 1

def randomize_quick_sort_part(array, p, r):
    """
    Рекурсивна частина рандомізованого швидкого сортування.
    :param array: Масив для сортування
    :param p: Початкова позиція
    :param r: Кінцева позиція
    """
    if p < r:
        q = randomize_partition(array, p, r)  # Випадкове розбиття масиву
        randomize_quick_sort_part(array, p, q - 1)  # Сортування лівої частини
        randomize_quick_sort_part(array, q + 1, r)  # Сортування правої частини

def randomize_quick_sort(array):
    """
    Основна функція рандомізованого швидкого сортування.
    :param array: Масив для сортування
    """
    randomize_quick_sort_part(array, 0, len(array) - 1)
import random
import time

def checkResult(array):
    """ Перевіряє впорядкованість масиву даних за зростанням
    :param array: масив
    """
    errors = 0
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            errors += 1

    print("Errors:       ", errors)

def testSort(method='randomize_quick'):
    assert method in ['merge', 'quick', 'randomize_quick']

    # Генеруємо випадковий масив
    s = [random.randint(-100000, 100000) for _ in range(N)]
    
    # Запускаємо сортування
    t = time.process_time()
    if method == 'randomize_quick':
        randomize_quick_sort(s)
    dt = time.process_time() - t
    
    print('Sorting time: ', dt)
    checkResult(s)

# Налаштування розміру масиву
N = 1000000

# Тестуємо рандомізоване швидке сортування
testSort(method="randomize_quick")
