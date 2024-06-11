# User Guide

**How to run the program:**

1. Ensure Python and Poetry are installed on your system.
2. Download the source code.
3. Open the command line and navigate to the directory containing the program.
4. Install dependencies by running: poetry install.
5. Run the program using the command 'python3 main.py text_file_path', replacing 'text_file_path' with the path to your text file. Use path to testtext.txt to run compressions on Kalevala text.
6. The program will run some tests automatically on the fly (including the data losslessness checks on both algorithms), providing validation for the implemented algorithms. Compression size results as well as time taken for compression is printed on the command line. 
7. Please see Tests documentation for information on running tests.