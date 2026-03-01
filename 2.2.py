dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
keys_set = set(dct.keys())
values_set = set(dct.values())
union_set = keys_set | values_set
print(f"Множество ключей: {keys_set}")
print(f"Множество значений: {values_set}")
print(f"Объединение множеств: {union_set}")