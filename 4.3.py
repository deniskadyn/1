def file_operations(text,filename):
    filename = "task3.txt"
    with open(filename, 'w') as file:
        file.write("Первая строка\n")
        file.write("Вторая строка\n")
        file.write("Третья строка\n")
        file.write("Четвертая строка\n")
    print("Файл создан!\n")
    text = "Пятая строка"
    with open(filename, 'a') as file:
        file.write(text + '\n')
    print("Текст добавлен!\n")
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Всего строк в файле: {len(lines)}")
        print("Четные строки:")
        for index, line in enumerate(lines):
            if index % 2 == 1:  # проверяем, что индекс нечетный
                print(f"  Строка {index + 1}: {line.strip()}")
file_operations()