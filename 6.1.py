def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

# Тесты
# 1. Тест с целыми числами
assert average_num([1, 1]) == 1

# 2. Тест с числами с плавающей точкой
assert average_num([2.5, 3.5]) == 3

# 3. Тест со смешанными целыми и вещественными числами
assert average_num([1, 2.5, 3, 4.5]) == 2.75

# 4. Тест с одним элементом
assert average_num([10]) == 10

# 5. Тест с отрицательными числами
assert average_num([-5, -3, -2]) == -3.33

# 6. Тест со строковыми цифрами (должны преобразоваться в int)
assert average_num(["5", "7", "9"]) == 7

# 7. Тест со смешанными типами (числа и строки-цифры)
assert average_num([1, "2", 3.5, "4"]) == 2.62

# 8. Тест с нулями
assert average_num([0, 0, 0, 0]) == 0

# 9. Тест с большими числами
assert average_num([1000, 2000, 3000]) == 2000

# 10. Тест с некорректными данными (должен вернуть "Bad request")
assert average_num([1, 2, "abc", 4]) == "Bad request"

print("Все тесты пройдены успешно!")