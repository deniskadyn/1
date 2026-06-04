import re

def is_palindrome(s: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.
    Игнорирует пробелы, знаки пунктуации и регистр букв.
    """
    # Приводим к нижнему регистру и оставляем только буквы и цифры
    cleaned = re.sub(r'[^a-zа-яё0-9]', '', s.lower())
    return cleaned == cleaned[::-1]

# Тесты
assert is_palindrome("Лёша на полке клопа нашёл") == True
assert is_palindrome("А роза упала на лапу Азора") == True
assert is_palindrome("Madam, I'm Adam") == True
assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("12321") == True
assert is_palindrome("Hello, World!") == False
assert is_palindrome("Не палиндром") == False
assert is_palindrome("") == True
assert is_palindrome("a") == True
assert is_palindrome("Коту тащат уток") == True

print("Все тесты пройдены успешно!")