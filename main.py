from compressor.compressor import check
from sys import argv
from compressor.generators.gentxt import generate_binary_file

if __name__ == "__main__":
    generate_binary_file()
    if len(argv) != 2:
        print("Usage: python3 main.py file_path")
    else:
        check(argv[1])