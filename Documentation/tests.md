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

Test coverage results

compressor/tests/test_compressor.py ............                                                                                                                                                                            [100%]

---------- coverage: platform darwin, python 3.10.6-final-0 ----------
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
compressor/__init__.py                    0      0   100%
compressor/compressor.py                165     64    61%
compressor/config.py                      2      0   100%
compressor/tests/__init__.py              0      0   100%
compressor/tests/test_compressor.py      48      0   100%
---------------------------------------------------------
TOTAL                                   215     64    70%