import random
import string
from pathlib import Path
folder = Path("random_files")
folder.mkdir(exist_ok=True)
for i in range(10):
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    name = name + ".txt"
    file = folder / name
    file.touch()
    print(file.absolute())