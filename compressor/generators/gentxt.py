from os import path
from ..config import BASE_PATH

def generate_binary_file():
    # Read from the text file
    with open(path.join(BASE_PATH, 'texts/text.txt'), 'rb') as file:
        #text = file.read()
        byte_content = file.read()
    # Convert the text to bytes
    #byte_content = text.encode()
    # Write the bytes to the binary file
    with open(path.join(BASE_PATH, 'texts/test.bin'), 'wb') as file:
        file.write(byte_content)

