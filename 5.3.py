import random
import json
import string
# Генерируем имя
first = random.choice(['John', 'Jane', 'Mike', 'Anna'])
last = random.choice(['Smith', 'Johnson', 'Brown'])
name = f"{first} {last}"
# Генерируем пароль (12 символов)
chars = string.ascii_letters + string.digits + string.punctuation
password = ''
for i in range(12):
    password += random.choice(chars)
# Создаем пользователя
user = {
    "name": name,
    "age": random.randint(18, 80),
    "email": name.lower().replace(' ', '.') + '@example.com',
    "password": password
}
# Сохраняем в файл
with open('user.json', 'w') as f:
    json.dump(user, f, indent=4)
# Читаем и выводим
with open('user.json', 'r') as f:
    print(json.dumps(json.load(f), indent=4))