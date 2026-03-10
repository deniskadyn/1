from typing import List
def multiply_list(numbers: List[int], multiplier: int = 2) -> List[int]:
    return [x * multiplier for x in numbers]
nums = [int(x) for x in input("Введите список чисел через пробел: ").split()]
mult = input("Введите множитель (по умолчанию 2): ")
if mult:
    mult = int(mult)
else:
    mult = 2
print(f"Результат (функция): {multiply_list(nums, mult)}")
print(f"Результат (лямбда): {list(map(lambda x: x * mult, nums))}")