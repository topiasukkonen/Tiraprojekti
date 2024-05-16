# Implementation

**General structure of the program:** The program is composed of several functions that each handle a specific task in the process of encoding, decoding, and calculating the size reduction.

- read_file(file_path, size=None): Reads n-bytes of binary data from a file and returns its content.
- write_file(file_path, data): Writes binary data to a file.
- huff_encode(msg): Encodes a message using Huffman coding and returns the encoded message, Huffman codes, and extra padding length.
- huff_decode(enc_msg, huff_c, extra_padding): Decodes a Huffman encoded message.
- lzw_encode(msg): Encodes a message using LZW compression and returns the encoded message and dictionary used for encoding.
- lzw_decode(comp_msg, dictionary): Decodes a LZW compressed message.
- size_reduction(original, compressed): Calculates the size reduction percentage after compression.
- print_compression_results(method, original, compressed, time_taken, file): Prints and logs the results of the compression method.
- check(file_path): Conducts compression tests on a file.

**Achieved time and space complexities:** Huffman and LZW encoding have a linear time complexity in the size of the input data.

**Performance analysis:** The program calculates the percentage reduction in size achieved by the Huffman and LZW algorithms and prints out the results.

**Possible improvements:** In future iterations of this project, other compression algorithms could be integrated, providing a broader understanding of the subject.

**References:**

- "Introduction to Algorithms", by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.
- Wikipedia articles on [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) and [LZW](https://en.wikipedia.org/wiki/Lempel–Ziv–Welch).
- Geeks for Geeks articles on [Huffman coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/) and [LZW](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/).