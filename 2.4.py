s = input("Введите строку: ")
s = s.lower()
words = s.split()
d = {}
for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1
for w, c in d.items():
    print(f"{w}: {c}")