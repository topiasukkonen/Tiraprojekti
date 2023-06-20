# User Guide

**How to run the program (basic):**

1. Ensure Python is installed on your system.
2. Download the source code.
3. Open the command line and navigate to the directory containing the program.
4. Run the program using the command 'python3 compressor.py binary_file_path', replacing 'binary_file_path' with the path to your binary file. Or, just run python3 compressor.py so it uses the default .bin in the root.

**How to run the program (advanced):**

You can provide natural language to the text.txt file. After that, you can run on the project root a command "python3 gentxt.py", which transforms the .txt file to binary format and saves it to test.bin. Also, random binary can be created using command "python3 genbin.py". Note that the genbin.py does not overwrite the test.bin content, so deletion of old binaries in the test.bin is recommended.

The program will run some tests automatically, providing validation for the implemented algorithms.
