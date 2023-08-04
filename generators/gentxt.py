def generate_binary_file():
    # Read from the text file
    with open('text.txt', 'r') as file:
        text = file.read()
    # Convert the text to bytes
    byte_content = text.encode()
    # Write the bytes to the binary file
    with open('test.bin', 'wb') as file:
        file.write(byte_content)
generate_binary_file()
