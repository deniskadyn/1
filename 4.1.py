from math import factorial
squares = [n**2 for n in range(1, 11)]
print("1. Квадраты чисел:", squares)

days = ["Понедельник", "Вторник", "Среда", "Четверг",
        "Пятница", "Суббота", "Воскресенье"]
week_dict = {day: i + 1 for i, day in enumerate(days)}
print("2. Дни недели:", week_dict)

libraries = ["Django", "FastAPI", "Numpy", "PYTHON",
             "Pandas", "FASTAPI", "Python", "random"]
tags = {lib.lower() for lib in libraries}
print("3. Теги библиотек:", tags)

numbers = [1, 3, 4, 87, 98, 15, 7, 4]
even_numbers = [num for num in numbers if num % 2 == 1]
print("4. нечетные числа:", even_numbers)

factorials = {n: factorial(n) for n in range(1, 6)}
print("5. Факториалы:", factorials)