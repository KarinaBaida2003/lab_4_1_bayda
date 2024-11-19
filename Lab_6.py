def flood_fill(matrix, x, y, new_color):
    # Отримуємо колір поточного пікселя
    original_color = matrix[x][y]
    
    # Якщо колір пікселя вже новий, нічого не робимо
    if original_color == new_color:
        return

    # Розміри матриці
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Функція для перевірки меж та кольору
    def is_valid(nx, ny):
        return 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == original_color
    
    # DFS для перефарбування
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        matrix[cx][cy] = new_color  # Перефарбовуємо
        
        # Додаємо сусідні пікселі у стек
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny):
                stack.append((nx, ny))

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Зчитування матриці з файлу
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

# Основна частина програми
def main():
    # Зчитуємо матрицю з файлу
    matrix = read_matrix_from_file('matrix.txt')
    
    # Початкова точка
    x0, y0 = 0, 1  # згідно з прикладом
    
    # Зчитуємо новий колір
    new_color = int(input("Введіть новий колір: "))
    
    # Виконуємо перефарбування
    flood_fill(matrix, x0, y0, new_color)
    
    # Виводимо нову матрицю
    print("Нова матриця:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
