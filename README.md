# Data Structures and Algorithms Project

In this project, the problem of data compression is addressed, focusing on compressing and decompressing binary data using Python. Two compression algorithms are implemented: Huffman Encoding and Lempel-Ziv-Welch (LZW). The primary data structures used include heaps, dictionaries, and lists.

The implementation features file handling capabilities, allowing the program to read and write to binary files. This should enable the compression of different file types, but testing of the compression has been done for text format data. The Huffman encoding process is utilizing a min-heap for Huffman tree construction. It includes functions for serializing and deserializing the Huffman tree, which allows the tree to be stored alongside the compressed data. The compressed data is written to a file in a custom format that includes the serialized Huffman tree, padding information, and the encoded data.

For LZW encoding, the implementation supports compression and decompression with a configurable maximum dictionary size, which is set to 6000 by default. The compressed data is stored as a list of integers, which are then written to a binary file. For each size increment, it compresses the data using both Huffman and LZW algorithms, then decompresses to verify data integrity. User can choose to use given testtext.txt as a compression file (which is Kalevala in a text format), or give his/her own text file. 

Error handling is incorporated, with the code raising a ValueError if decoding fails due to bad compressed code. Performance metrics are calculated and reported, including the compression ratio (expressed as the compressed size as a percentage of the original size) and the time taken for compression for both algorithms.

The code writes compressed data to binary files in designated 'packedHuff' and 'packedLZW' directories. For verification purposes, decompressed data is written to text files in the same directories.

In this project, I've tackled the problem of data compression, focusing specifically on text data and using Python as my language of choice for implementation.

Two different algorithms were utilized for the compression task: Huffman Encoding and Lempel-Ziv-Welch (LZW) Encoding. Heaps and dictionaries are the primary data structures used throughout this project.

The Python script accepts a text file as an input, performs Huffman and LZW encoding methods to compress the file, and subsequently decompresses the data back to the original form. User can choose to use given testtext.txt as a compression file (which is Kalevala in a text format), or give his/her own text file. The program then runs compressions from 2 byte size up to the size the user wants (see compressor.py code documentation for MAX_SIZE variable).

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