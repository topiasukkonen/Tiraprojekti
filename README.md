# Data Structures and Algorithms Project

In this project, I've tackled the problem of data compression, focusing specifically on binary data and using Python as my language of choice for implementation.

Two different algorithms were utilized for the compression task: Huffman Encoding and Lempel-Ziv-Welch (LZW) Encoding. Huffman Encoding generates variable-length bit patterns for each unique byte, depending on their frequency of occurrence, whereas LZW Encoding doesn't require prior knowledge of the input data distribution, making it a versatile choice for data compression tasks.

Heaps and dictionaries are the primary data structures used throughout this project.

The Python script accepts a binary file as an input, performs Huffman and LZW encoding methods to compress the file, and subsequently decompresses the data back to the original form. This showcases the lossless nature of these compression techniques.

To assess the robustness and correctness of the algorithms, a suite of tests is included in the script. These tests ensure that the original binary data is equivalent to the decompressed data following compression and decompression - a critical check for any compression-decompression system.

In addition to the compression-decompression process, the program also provides information about the effectiveness of the compression. It calculates and outputs the percentage reduction in binary data size achieved by the Huffman and LZW algorithms. Also, time taken by each algorithm is provided to the user.

Here's how you can run the program:

1. Ensure Python is installed on your system.
2. Download the source code.
3. Open the command line and navigate to the directory containing the program.
4. Run the program using the command 'python3 compressor.py binary_file_path', replacing 'binary_file_path' with the path to your binary file.
5. The program will run some tests automatically, providing validation for the implemented algorithms.

You can find the program on GitHub. Future iterations of this project may include the integration of more compression algorithms, providing an even broader understanding of the subject.

Example results on file sizes given below:

569 kb: 

Huffman: Compressed equals the original one.
Huffman reduced the size by 43.84192985909948%
Huffman compression took 0.1880629062652588 seconds.
LZW: Compressed equals the original one.
LZW reduced the size by 8.163301178389627%
LZW compression took 0.11291384696960449 seconds.
Passed all tests!

1,1 mb:

Huffman: Compressed equals the original one.
Huffman reduced the size by 43.841891327752506%
Huffman compression took 0.36904406547546387 seconds.
LZW: Compressed equals the original one.
LZW reduced the size by 12.294333487135543%
LZW compression took 0.22165179252624512 seconds.
Passed all tests!

2,3 mb:

Huffman: Compressed equals the original one.
Huffman reduced the size by 43.84192141772054%
Huffman compression took 0.7337138652801514 seconds.
LZW: Compressed equals the original one.
LZW reduced the size by 16.037946031314966%
LZW compression took 0.478085994720459 seconds.
Passed all tests!

500 kb:

Huffman: Compressed equals the original one.
Huffman reduced the size by 43.853200834914304%
Huffman compression took 0.16410613059997559 seconds.
LZW: Compressed equals the original one.
LZW reduced the size by 7.3540187182401855%
LZW compression took 0.09888887405395508 seconds.
Passed all tests!

400 kb: 

Huffman: Compressed equals the original one.
Huffman reduced the size by 43.907267198628595%
Huffman compression took 0.13195419311523438 seconds.
LZW: Compressed equals the original one.
LZW reduced the size by 5.015713965021122%
LZW compression took 0.07528877258300781 seconds.
Passed all tests!

4,6 mb:

Huffman: Compressed equals the original one.
Huffman reduced the size by 43.84192141772054%
Huffman compression took 1.4597809314727783 seconds.
LZW: Compressed equals the original one.
LZW reduced the size by 21.36498842310317%
LZW compression took 1.0604040622711182 seconds.
Passed all tests!

6,8 mb

Huffman: Compressed equals the original one.
Huffman reduced the size by 43.84192964364813%
Huffman compression took 2.1795170307159424 seconds.
LZW: Compressed equals the original one.
LZW reduced the size by 25.35991129287413%
LZW compression took 1.7601299285888672 seconds.
Passed all tests!

# Further Documentation

- [Implementation](https://github.com/topiasukkonen/Tiraprojekti/blob/main/Documentation/implementation.md)
- [Spesifications](https://github.com/topiasukkonen/Tiraprojekti/blob/main/Documentation/specs.md)
- [Tests](https://github.com/topiasukkonen/Tiraprojekti/blob/main/Documentation/tests.md)
- [User Guide](https://github.com/topiasukkonen/Tiraprojekti/blob/main/Documentation/userguide.md)

**References:**

- Python Language Reference, version 3.7. Available at http://www.python.org
- "Introduction to Algorithms", by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.
- Wikipedia articles on [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) and [LZW](https://en.wikipedia.org/wiki/Lempel–Ziv–Welch).
- Geeks for Geeks articles on [Huffman coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/) and [LZW](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/).
