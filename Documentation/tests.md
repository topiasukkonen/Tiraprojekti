## Testing

### Introduction
This document describes the testing process for the Tiraprojekti project. We use the `pytest` framework for creating and running tests, and `pytest-cov` to measure test coverage.

### Dependencies
The project uses the following testing dependencies:

- pytest: This is our testing framework.
- pytest-cov: This plugin for pytest generates test coverage reports.

These dependencies are listed as development dependencies in the Poetry project file (`pyproject.toml`).

### Test Structure
The tests are located in the `test_compressor.py` file. This file contains unit tests for the functionality provided by the `compressor.py` module. The following functions are tested:

- `read_file()`
- `huff_encode()`
- `huff_decode()`
- `lzw_encode()`
- `lzw_decode()`
- `size_red()`

Each function in `compressor.py` should have corresponding test cases in `test_compressor.py`.

### Running Tests
To run the tests, first navigate to the project's root directory (`Tiraprojekti`) in your terminal. 

Ensure that the virtual environment created by Poetry is activated:

```bash
poetry shell
```

Then, use the following command to run the tests:

```bash
pytest test_compressor.py
```

`pytest` will automatically discover all the tests in `test_compressor.py` and run them.

### Test Coverage
To generate a test coverage report, use the `pytest-cov` plugin. The following command will run the tests and print a coverage report in the terminal:

```bash
pytest --cov=compressor test_compressor.py
```

This command tells `pytest` to measure the test coverage of the `compressor.py` module and print a report.

You can also generate a more detailed HTML coverage report. The following command will generate the report and save it in a directory named `htmlcov`:

```bash
pytest --cov=compressor --cov-report=html test_compressor.py
```

You can view the HTML report by opening `htmlcov/index.html` in a web browser.