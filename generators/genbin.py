import os

data = os.urandom(19024)

with open('test.bin', 'wb') as f:
    f.write(data)
