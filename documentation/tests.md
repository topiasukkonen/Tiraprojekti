## Testing

### Compressing test results

Example results on file sizes given below:

Compressing 2 bytes (0.00 KB, 0.00 MB)
Huffman reduced the size by 50.00%
Huffman compression took 0.0001 seconds.
LZW reduced the size by -900.00%
LZW compression took 0.0001 seconds.

----------
Compressing 4 bytes (0.00 KB, 0.00 MB)
Huffman reduced the size by 50.00%
Huffman compression took 0.0000 seconds.
LZW reduced the size by -500.00%
LZW compression took 0.0001 seconds.

----------
Compressing 8 bytes (0.01 KB, 0.00 MB)
Huffman reduced the size by 62.50%
Huffman compression took 0.0000 seconds.
LZW reduced the size by -300.00%
LZW compression took 0.0001 seconds.

----------
Compressing 16 bytes (0.02 KB, 0.00 MB)
Huffman reduced the size by 56.25%
Huffman compression took 0.0001 seconds.
LZW reduced the size by -193.75%
LZW compression took 0.0001 seconds.

----------
Compressing 32 bytes (0.03 KB, 0.00 MB)
Huffman reduced the size by 46.88%
Huffman compression took 0.0001 seconds.
LZW reduced the size by -146.88%
LZW compression took 0.0001 seconds.

----------
Compressing 64 bytes (0.06 KB, 0.00 MB)
Huffman reduced the size by 43.75%
Huffman compression took 0.0001 seconds.
LZW reduced the size by -115.62%
LZW compression took 0.0001 seconds.

----------
Compressing 128 bytes (0.12 KB, 0.00 MB)
Huffman reduced the size by 43.75%
Huffman compression took 0.0001 seconds.
LZW reduced the size by -89.84%
LZW compression took 0.0001 seconds.

----------
Compressing 256 bytes (0.25 KB, 0.00 MB)
Huffman reduced the size by 43.75%
Huffman compression took 0.0002 seconds.
LZW reduced the size by -73.05%
LZW compression took 0.0002 seconds.

----------
Compressing 512 bytes (0.50 KB, 0.00 MB)
Huffman reduced the size by 43.16%
Huffman compression took 0.0003 seconds.
LZW reduced the size by -60.35%
LZW compression took 0.0002 seconds.

----------
Compressing 1024 bytes (1.00 KB, 0.00 MB)
Huffman reduced the size by 43.85%
Huffman compression took 0.0002 seconds.
LZW reduced the size by -45.80%
LZW compression took 0.0004 seconds.

----------
Compressing 2048 bytes (2.00 KB, 0.00 MB)
Huffman reduced the size by 44.19%
Huffman compression took 0.0004 seconds.
LZW reduced the size by -33.79%
LZW compression took 0.0007 seconds.

----------
Compressing 4096 bytes (4.00 KB, 0.00 MB)
Huffman reduced the size by 44.36%
Huffman compression took 0.0007 seconds.
LZW reduced the size by -22.41%
LZW compression took 0.0012 seconds.

----------
Compressing 8192 bytes (8.00 KB, 0.01 MB)
Huffman reduced the size by 44.59%
Huffman compression took 0.0011 seconds.
LZW reduced the size by -10.47%
LZW compression took 0.0023 seconds.

----------
Compressing 16384 bytes (16.00 KB, 0.02 MB)
Huffman reduced the size by 44.33%
Huffman compression took 0.0022 seconds.
LZW reduced the size by 0.63%
LZW compression took 0.0047 seconds.

----------
Compressing 32768 bytes (32.00 KB, 0.03 MB)
Huffman reduced the size by 43.94%
Huffman compression took 0.0046 seconds.
LZW reduced the size by 10.46%
LZW compression took 0.0102 seconds.

----------
Compressing 65536 bytes (64.00 KB, 0.06 MB)
Huffman reduced the size by 43.98%
Huffman compression took 0.0088 seconds.
LZW reduced the size by 19.26%
LZW compression took 0.0200 seconds.

----------
Compressing 131072 bytes (128.00 KB, 0.12 MB)
Huffman reduced the size by 43.85%
Huffman compression took 0.0176 seconds.
LZW reduced the size by 26.92%
LZW compression took 0.0410 seconds.

----------
Compressing 262144 bytes (256.00 KB, 0.25 MB)
Huffman reduced the size by 43.88%
Huffman compression took 0.0358 seconds.
LZW reduced the size by 33.39%
LZW compression took 0.0795 seconds.

----------
Compressing 524288 bytes (512.00 KB, 0.50 MB)
Huffman reduced the size by 43.86%
Huffman compression took 0.0727 seconds.
LZW reduced the size by 35.67%
LZW compression took 0.1667 seconds.

----------
Compressing 1048576 bytes (1024.00 KB, 1.00 MB)
Huffman reduced the size by 43.84%
Huffman compression took 0.1428 seconds.
LZW reduced the size by 35.37%
LZW compression took 0.3387 seconds.

----------
Compressing 2097152 bytes (2048.00 KB, 2.00 MB)
Huffman reduced the size by 43.85%
Huffman compression took 0.3693 seconds.
LZW reduced the size by 35.01%
LZW compression took 0.7956 seconds.

----------
Compressing 4194304 bytes (4096.00 KB, 4.00 MB)
Huffman reduced the size by 43.84%
Huffman compression took 0.6141 seconds.
LZW reduced the size by 37.04%
LZW compression took 1.5826 seconds.

----------

### Introduction
This document describes the testing process for the Tiraprojekti project. Pytest is the main test framework used.

### Dependencies
The project uses the following testing dependencies:

- pytest
- pytest-cov

These dependencies are listed as development dependencies in the Poetry project file (`pyproject.toml`).

### Test Structure
The tests are located in the `test_compressor.py` file (compressor/tests/test_compressor.py). This file contains unit tests for the functionality provided by the `compressor.py` module. The following functions are tested:

- read_file()
- huff_encode()
- huff_decode()
- lzw_encode()
- lzw_decode()
- size_reduction()

### Running Tests
To run the tests, first navigate to the project's root directory (`tiraprojekti`) in your terminal. 

Use the following command to run the tests:

```bash
pytest compressor/tests/test_compressor.py
```

`pytest` will automatically discover all the tests in `test_compressor.py` and run them.

### Test Coverage

Use the following command to run the tests with coverage:

```bash
pytest pytest --cov=compressor
```

---------- coverage: platform darwin, python 3.10.6-final-0 ----------
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
compressor/__init__.py                    0      0   100%
compressor/compressor.py                119     36    70%
compressor/config.py                      2      0   100%
compressor/tests/__init__.py              0      0   100%
compressor/tests/test_compressor.py      56      0   100%
---------------------------------------------------------
TOTAL                                   177     36    80%
