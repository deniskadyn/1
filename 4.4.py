def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        print(f"Площадь прямоугольника: {func(*args, **kwargs)}")
    return wrapper
@decorator
def area(a, b):
    return a * b
area(5, 10)