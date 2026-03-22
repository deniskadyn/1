import random
from datetime import datetime, timedelta
import array
today = datetime.now()
dates = []
# Создаем 10 случайных дат
for i in range(10):
    days = random.randint(0, 1825)  # 5 лет = 1825 дней
    dates.append(today - timedelta(days=days))
dates.sort()  # сортируем по возрастанию
# Массив для разниц
diffs = array.array('i')
# Считаем разницы
for i in range(9):  # 9 пар для 10 дат
    d1 = dates[i].strftime("%Y-%m-%d")
    d2 = dates[i+1].strftime("%Y-%m-%d")
    diff = (dates[i+1] - dates[i]).days
    diffs.append(diff)
    print(f"Разница между {d1} и {d2}: {diff} дней")

print("\nМассив разниц:", diffs.tolist())