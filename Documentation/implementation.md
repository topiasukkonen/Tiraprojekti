
# Implementation

**General structure of the program:** The program is composed of several functions that each handle a specific task in the process of encoding, decoding, and calculating the size reduction.

- `read_file(file_path)`: Reads a binary file and returns its content.
- `huff_encode(msg)`, `huff_decode(enc_msg, huff_c)`: Implement Huffman encoding and decoding, respectively.
- `lzw_encode(msg)`, `lzw_decode(comp_msg, dict_)`: Implement LZW encoding and decoding, respectively.
- `size_red(orig, comp)`: Calculates the size reduction as a percentage after compression.

**Achieved time and space complexities:** Huffman and LZW encoding have a linear time complexity in the size of the input data. However, the space complexity can be higher, depending on the diversity of the input data.

**Performance analysis:** The program calculates the percentage reduction in size achieved by the Huffman and LZW algorithms and prints out the results.

**Possible improvements:** In future iterations of this project, other compression algorithms could be integrated, providing a broader understanding of the subject.

**References:**

- "Introduction to Algorithms", by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.
- Wikipedia articles on [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) and [LZW](https://en.wikipedia.org/wiki/Lempel–Ziv–Welch).
- Geeks for Geeks articles on [Huffman coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/) and [LZW](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/).