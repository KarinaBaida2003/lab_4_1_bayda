def check_brackets(s: str) -> bool:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in brackets.values():  # якщо це відкрита дужка
            stack.append(char)
        elif char in brackets.keys():  # якщо це закрита дужка
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
    
    return len(stack) == 0  # перевіряємо, чи стек порожній

# Тестування
if check_brackets("([])"):
    print("Правильно розставлені")
else:
    print("Неправильно розставлені")

def tests():
    assert check_brackets("(2+3]*[3-2)") is False
    assert check_brackets("([34+54.5]-{3+(2.1-1.2}))") is False
    assert check_brackets(") + (2-3)") is False
    assert check_brackets("(2+(3-5))[4-{2+2}]") is True
    assert check_brackets("([34+54.5]-{3+(2.1-1.2)})") is True
    assert check_brackets(")") is False
    assert check_brackets("[)") is False
    assert check_brackets("(){}[]{}[]") is True
    assert check_brackets("(((())))") is True
    assert check_brackets("((((){}[]{}[])))") is True
    assert check_brackets("(((())") is False
    assert check_brackets("())))") is False
    assert check_brackets("(){}[]{}[])))") is False

tests()
