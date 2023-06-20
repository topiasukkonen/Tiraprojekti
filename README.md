# Documentation
implementation.md


# Data Structures and Algorithms Project

In this project, I've tackled the problem of data compression, focusing specifically on binary data and using Python as my language of choice for implementation.

Two different algorithms were utilized for the compression task: Huffman Encoding and Lempel-Ziv-Welch (LZW) Encoding. Huffman Encoding generates variable-length bit patterns for each unique byte, depending on their frequency of occurrence, whereas LZW Encoding doesn't require prior knowledge of the input data distribution, making it a versatile choice for data compression tasks.

Heaps and dictionaries are the primary data structures used throughout this project.

The Python script accepts a binary file as an input, performs Huffman and LZW encoding methods to compress the file, and subsequently decompresses the data back to the original form. This showcases the lossless nature of these compression techniques.

To assess the robustness and correctness of the algorithms, a suite of tests is included in the script. These tests ensure that the original binary data is equivalent to the decompressed data following compression and decompression - a critical check for any compression-decompression system.

In addition to the compression-decompression process, the program also provides information about the effectiveness of the compression. It calculates and outputs the percentage reduction in binary data size achieved by the Huffman and LZW algorithms.

Here's how you can run the program:

1. Ensure Python is installed on your system.
2. Download the source code.
3. Open the command line and navigate to the directory containing the program.
4. Run the program using the command 'python3 compressor.py binary_file_path', replacing 'binary_file_path' with the path to your binary file.
5. The program will run some tests automatically, providing validation for the implemented algorithms.

You can find the program on GitHub. Future iterations of this project may include the integration of more compression algorithms, providing an even broader understanding of the subject.

Example results on the same binary file present in the current project:

Huffman: Compressed equals the original one.
Huffman reduced the size by -683.69140625%
LZW: Compressed equals the original one.
LZW reduced the size by -155.56640625%
Passed all tests!

**References:**

- Python Language Reference, version 3.7. Available at http://www.python.org
- "Introduction to Algorithms", by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.
- Wikipedia articles on [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) and [LZW](https://en.wikipedia.org/wiki/Lempel–Ziv–Welch).
- Geeks for Geeks articles on [Huffman coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/) and [LZW](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/).
