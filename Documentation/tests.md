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
pytest --cov=compressor
```

### Test coverage results

- [Coverage](https://github.com/topiasukkonen/Tiraprojekti/blob/main/Documentation/testCoverage.jpeg)