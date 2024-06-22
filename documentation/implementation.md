# Implementation

**General structure of the program**

The program consists of several functions that handle specific tasks in the process of encoding, decoding, and analyzing data compression using Huffman and LZW algorithms. It can read and write binary data, allowing for compression of any file type.

**Functions**

- `read_file(file_path, size=None)`: Reads binary data from a file, with an optional size limit.
- `write_file(file_path, data)`: Writes binary data to a file.
- `huff_encode(input)`: Performs Huffman encoding on input bytes, returning encoded bytes, Huffman codes, and padding length.
- `huff_decode(encoded_bytes, huffman_codes, padding_length)`: Decodes Huffman-encoded data.
- `serialize_huffman_tree(tree)`: Serializes the Huffman tree for storage.
- `deserialize_huffman_tree(serialized_tree)`: Deserializes the Huffman tree from storage.
- `write_huffman_compressed(file_path, encoded_bytes, huffman_codes, padding_length)`: Writes Huffman-compressed data to a file.
- `read_huffman_compressed(file_path)`: Reads Huffman-compressed data from a file.
- `lzw_encode(input_data, max_dict_size=6000)`: Performs LZW encoding on input bytes.
- `lzw_decode(encoded_input, max_dict_size=6000)`: Decodes LZW-encoded data.
- `write_compressed_to_file(comp_msg, file_path)`: Writes LZW-compressed data to a file.
- `read_compressed_from_file(file_path)`: Reads LZW-compressed data from a file.
- `size_reduction(original, compressed)`: Calculates the compression ratio.
- `print_compression_results(method, original, compressed, time_taken, file, additional_size=0)`: Prints and logs compression results.
- `check(file_path)`: Conducts compression tests on a file, incrementally increasing the data size up to 20 MB.

**Achieved time and space complexities**

Time and space complexity should be O(n) for both algorithms.

**Performance analysis**

The program calculates and reports the compression ratio (compressed size as a percentage of original size) and the time taken for both Huffman and LZW compression. It performs these calculations for increasingly larger portions of the input file, up to value set to MAX_SIZE variable (default 20 MB).

**Possible improvements:** In future iterations of this project, other compression algorithms could be integrated, providing a broader understanding of the subject.

**References:**

- "Introduction to Algorithms", by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. (https://dl.ebooksworld.ir/books/Introduction.to.Algorithms.4th.Leiserson.Stein.Rivest.Cormen.MIT.Press.9780262046305.EBooksWorld.ir.pdf)
- Wikipedia articles on [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) and [LZW](https://en.wikipedia.org/wiki/Lempel–Ziv–Welch).
- Geeks for Geeks articles on [Huffman coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/) and [LZW](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/).