import os

data = os.urandom(19024)  # 1024 bytes of random data

with open('test.bin', 'wb') as f:
    f.write(data)
