def evaluatePrefix(expression: str) -> int:
    # Ініціалізуємо стек
    stack = []
    
    # Розділяємо вираз на частини (числа і оператори)
    tokens = expression.split()
    
    # Проходимо через токени справа наліво
    for token in reversed(tokens):
        if token in "+-*/":
            # Якщо токен - оператор, витягуємо два операнди зі стеку
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 // operand2  # Цілочисельне ділення
            # Поміщаємо результат назад у стек
            stack.append(result)
        else:
            # Якщо токен - число, перетворюємо його в int і кладемо в стек
            stack.append(int(token))
    
    # В стеку залишиться один елемент - результат
    return stack.pop()

# Приклад використання
expression = "- + 10 * 3 2 6"
result = evaluatePrefix(expression)
print(result)  # Виведе: 10
