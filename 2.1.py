text = input("Введите числа через пробел: ")
items = text.split()
a = int(input("Введите степень: "))
b = []
for x in items:
    if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
        n = int(x)
        b.append(n ** a)
    else:
        b.append(x * a)
print("Вывод:", end=" ")
for y in b:
    print(y, end=" ")