import math
def summ(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Оба аргумента должны быть числами")
    return a + b

def minus(a, b):
    if not isinstance(a,int) or not isinstance(b, int):
        raise TypeError("Оба аргумента должны быть числами")
    return a - b

def multiply(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Оба аргумента должны быть числами")
    return a * b

def divide(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

def int_divide(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a // b

def mod_divide(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a % b


def power(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Оба аргумента должны быть числами")
    return a ** b

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Факториал можно вычислить только для целого числа")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def square_root(x):
    if not isinstance(x, int):
        raise TypeError("Аргумент должен быть числом")
    if x < 0:
        raise ValueError("Квадратный корень из отрицательного числа не извлекается")
    return math.sqrt(x)

def average():
    numbers_str = input("Введите числа через пробел: ")
    parts = numbers_str.split()
    if not parts:
        raise ValueError("Список чисел не может быть пустым")

    numbers = []
    for part in parts:
        try:
            if '.' in part:
                numbers.append(float(part))
            else:
                numbers.append(int(part))
        except ValueError:
            raise TypeError(f"'{part}' не является числом")

    return sum(numbers) / len(numbers)

while True:
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление (обычное)")
    print("5. Деление (целочисленное)")
    print("6. Деление (остаток)")
    print("7. Возведение в степень")
    print("8. Факториал")
    print("9. Квадратный корень")
    print("10. Среднее арифметическое")
    print("Для выхода введите 'exit' ")
    choice = input("Операция: ")
    if choice.lower() == 'exit' :
        break
    try:
        if choice == '1':  # Сложение
            a = int(input("Слагаемое 1: "))
            b = int(input("Слагаемое 2: "))
            result = summ(a, b)
            print(f"Результат: {result}")

        elif choice == '2':  # Вычитание
            a = int(input("Уменьшаемое: "))
            b = int(input("Вычитаемое: "))
            result = minus(a, b)
            print(f"Результат: {result}")

        elif choice == '3':  # Умножение
            a = int(input("Множитель 1: "))
            b = int(input("Множитель 2: "))
            result = multiply(a, b)
            print(f"Результат: {result}")

        elif choice == '4':  # Обычное деление
            a = int(input("Делимое: "))
            b = int(input("Делитель: "))
            result = divide(a, b)
            print(f"Результат: {result}")

        elif choice == '5':  # Целочисленное деление
            a = int(input("Делимое: "))
            b = int(input("Делитель: "))
            result = int_divide(a, b)
            print(f"Результат: {result}")

        elif choice == '6':  # Остаток от деления
            a = int(input("Делимое: "))
            b = int(input("Делитель: "))
            result = mod_divide(a, b)
            print(f"Результат: {result}")

        elif choice == '7':  # Возведение в степень
            a = int(input("Основание: "))
            b = int(input("Показатель степени: "))
            result = power(a, b)
            print(f"Результат: {result}")

        elif choice == '8':  # Факториал
            n = int(input("Число для факториала: "))
            result = factorial(n)
            print(f"Результат: {result}")

        elif choice == '9':  # Квадратный корень
            x = int(input("Число для квадратного корня: "))
            result = square_root(x)
            print(f"Результат: {result}")

        elif choice == '10':  # Среднее арифметическое
            result = average()
            print(f" Результат: {result}")

        else:
            print("Ошибка: неизвестная операция. Выберите номер от 1 до 10")

    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")