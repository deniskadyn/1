import random, statistics, math
# Генерируем числа
nums = [random.randint(1, 100) for i in range(100)]
# Вычисляем и выводим
print(f"Среднее: {round(statistics.mean(nums), 2)}, "
      f"Медиана: {round(statistics.median(nums), 2)}, "
      f"Стандартное отклонение: {round(statistics.stdev(nums), 2)}, "
      f"Корень из суммы: {round(math.sqrt(sum(nums)), 2)}")