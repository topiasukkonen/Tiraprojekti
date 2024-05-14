from os import path, urandom
from ..config import BASE_PATH

data = urandom(19024)

with open(path.join(BASE_PATH, 'texts/test.bin'), 'wb') as f:
    f.write(data)
