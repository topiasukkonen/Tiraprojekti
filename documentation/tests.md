## Testing

### Compressing test results

See results.txt

### Introduction
This document describes the testing process for the Tiraprojekti project. Pytest is the main test framework used.

### Dependencies
The project uses the following testing dependencies:

- pytest
- pytest-cov

These dependencies are listed as development dependencies in the Poetry project file (`pyproject.toml`).

### Test Structure
The tests are located in the `test_compressor.py` file. This file contains comprehensive unit tests for the functionality provided by the compressor module. The following areas are tested:

- File I/O operations (read_file(), write_file())
- Huffman encoding and decoding (huff_encode(), huff_decode())
- LZW compression and decompression (lzw_encode(), lzw_decode())
- Huffman tree serialization and deserialization
- Size reduction calculation
- Performance on large files
- Handling of different data types (ASCII, Unicode, binary)
- Error handling and edge cases
- Compression with limited dictionary size for LZW

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
pytest --cov=compressor
```

### Test coverage results

See testCoverage.jpeg on this folder. 