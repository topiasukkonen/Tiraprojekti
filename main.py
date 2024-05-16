from compressor.compressor import check
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 main.py file_path")
    else:
        check(argv[1])