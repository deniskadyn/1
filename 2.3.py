a = input("Введите первый список: ")
b = input("Введите второй список: ")
a1 = a.split()
b1 = b.split()
a2 = []
b2 = []
for x in a1:
    a2.append(int(x))
for x in b1:
    b2.append(int(x))
s1 = set(a2)
s2 = set(b2)
c = s1 & s2
print("Общие элементы:", end=" ")
for x in c:
    print(x, end=" ")