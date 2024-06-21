# Data Structures and Algorithms Project

In this project, I've tackled the problem of data compression, focusing specifically on text data and using Python as my language of choice for implementation.

Two different algorithms were utilized for the compression task: Huffman Encoding and Lempel-Ziv-Welch (LZW) Encoding. Huffman Encoding generates variable-length bit patterns for each unique byte, depending on their frequency of occurrence, whereas LZW Encoding doesn't require prior knowledge of the input data distribution, making it a versatile choice for data compression tasks.

Heaps and dictionaries are the primary data structures used throughout this project.

The Python script accepts a text file as an input, performs Huffman and LZW encoding methods to compress the file, and subsequently decompresses the data back to the original form. This showcases the lossless nature of these compression techniques. User can choose to use given testtext.txt as a compression file, or give his/her own text file. The program then runs compressions from 2 byte size up to the size the user wants (see compressor.py code documentation for MAX_SIZE variable).

To assess the robustness and correctness of the algorithms, a suite of tests is included in the script. These tests ensure that the original text data is equivalent to the decompressed data following compression and decompression.

In addition to the compression-decompression process, the program also provides information about the effectiveness of the compression. It calculates and outputs the percentage reduction in text data size achieved by the Huffman and LZW algorithms. Also, time taken by each algorithm is provided to the user.

After compressions, decoded text files in tandem with compressed binary files are provided on the packedLZW and packedHuff folders to assure data losslessness. For Huffman, tree structure is provided on a separate file. 

Here's how you can run the program:

1. Ensure Python and Poetry are installed on your system.
2. Download the source code.
3. Open the command line and navigate to the directory containing the program.
4. Install dependencies by running: poetry install.
5. Run the program using the command 'python3 main.py text_file_path', replacing 'text_file_path' with the path to your text file. Use path to testtext.txt to run compressions on Kalevala text.
6. The program will run some tests automatically on the fly (including the data losslessness checks on both algorithms), providing validation for the implemented algorithms. Compression size results as well as time taken for compression is printed on the command line and also saved to results.txt.
7. Please see Tests documentation for information on running tests.

# Further Documentation

- [Implementation](https://github.com/topiasukkonen/Tiraprojekti/blob/main/documentation/implementation.md)
- [Spesifications](https://github.com/topiasukkonen/Tiraprojekti/blob/main/documentation/specs.md)
- [Tests](https://github.com/topiasukkonen/Tiraprojekti/blob/main/documentation/tests.md)
- [User Guide](https://github.com/topiasukkonen/Tiraprojekti/blob/main/documentation/userguide.md)