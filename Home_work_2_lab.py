def find_first(array, x):
    low, high = 0, len(array) - 1
    first_occurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            first_occurrence = mid
            high = mid - 1  # Продовжуємо пошук в лівій частині
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return first_occurrence

def find_last(array, x):
    low, high = 0, len(array) - 1
    last_occurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            last_occurrence = mid
            low = mid + 1  # Продовжуємо пошук в правій частині
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return last_occurrence

def counter(array, x):
    """ Кількість входжень заданого числа.
    :param array: Масив цілих чисел, впорядкований за неспаданням
    :param x:     Шуканий елемент
    :return:      Кількість входжень
    """
    first_index = find_first(array, x)
    if first_index == -1:  # Елемент не знайдено
        return 0
    
    last_index = find_last(array, x)
    
    return last_index - first_index + 1

from random import randint
from time import process_time
from collections import Counter

# Функції для пошуку першого і останнього входження числа
def find_first(array, x):
    low, high = 0, len(array) - 1
    first_occurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            first_occurrence = mid
            high = mid - 1  # Продовжуємо пошук в лівій частині
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return first_occurrence

def find_last(array, x):
    low, high = 0, len(array) - 1
    last_occurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            last_occurrence = mid
            low = mid + 1  # Продовжуємо пошук в правій частині
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return last_occurrence

def counter(array, x):
    """ Кількість входжень заданого числа.
    :param array: Масив цілих чисел, впорядкований за неспаданням
    :param x:     Шуканий елемент
    :return:      Кількість входжень
    """
    first_index = find_first(array, x)
    if first_index == -1:  # Елемент не знайдено
        return 0
    
    last_index = find_last(array, x)
    
    return last_index - first_index + 1

# Функція для тестування
def test(TestName, N, M):
    arr = [randint(0, M - 1) for _ in range(N)]
    arr.sort()

    # Створюємо словник для підрахунку кількості входжень
    d = Counter(arr)

    errors = 0
    dt = process_time()
    for _ in range(N):
        v = randint(0, M - 1)

        r = counter(arr, v)

        if v not in d and r > 0:
            errors += 1
        elif v in d and r != d[v]:
            errors += 1

    dt = process_time() - dt
    print(TestName, " Errors: %6d" % errors, " Running time: %2.5f" % dt)

# Запуск тестів
test("TEST #1", 100000, 100000)
test("TEST #2", 100, 100000)
test("TEST #3", 100000, 100)


