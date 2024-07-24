import pytest
import os
from time import time
from ..config import BASE_PATH
from ..compressor import * 


# Paths for test files
test_file = os.path.join(BASE_PATH, 'texts', 'testtext.txt')


# Sample data for testing
@pytest.fixture
def sample_data():
    return read_file(test_file)

@pytest.fixture
def large_data():
    return os.urandom(1024 * 1024 * 10)

# Test read and write
def test_read_write_file(tmp_path, sample_data):
    test_file = tmp_path / "test.bin"
    write_file(str(test_file), sample_data)
    assert read_file(str(test_file)) == sample_data, "File read/write failed"

# Huffman encoding and decoding with different types of data
@pytest.mark.parametrize('data', [
    b'ASCII text',
    'sdssdgнгs Unicode sdsd'.encode('utf-8'),
    os.urandom(100),  # Binary
    b''  # Empty
])
def test_huffman_codec(data):
    enc_data, huff_c, padding = huff_encode(data)
    assert huff_decode(enc_data, huff_c, padding) == data, "Huffman codec failed"
# LZW encoding and decoding with different types of data
@pytest.mark.parametrize('data', [
    b'ASCII text',
    'Неоо теста'.encode('utf-8'),
    os.urandom(100),  # Binary
    b''  # Empty
])
def test_lzw_codec(data):
    comp_data, _ = lzw_encode(data)
    assert lzw_decode(comp_data) == data, "LZW codec failed"

# Loading Huffman-compressed data correctly
def test_huffman_file_io(tmp_path, sample_data):
    compressed_file = tmp_path / "huffman.bin"
    enc_data, huff_c, padding = huff_encode(sample_data)
    write_huffman_compressed(str(compressed_file), enc_data, huff_c, padding)
    
    read_enc_data, read_huff_c, read_padding = read_huffman_compressed(str(compressed_file))
    assert huff_decode(read_enc_data, read_huff_c, read_padding) == sample_data, "Huffman file I/O failed"

# Loading LZW-compressed data correctly
def test_lzw_file_io(tmp_path, sample_data):
    compressed_file = tmp_path / "lzw.bin"
    comp_data, _ = lzw_encode(sample_data)
    write_compressed_to_file(comp_data, str(compressed_file))
    
    read_comp_data = read_compressed_from_file(str(compressed_file))
    assert lzw_decode(read_comp_data) == sample_data, "LZW file I/O failed"

# Serialize and deserialize Huffman trees correctly
def test_huffman_tree_serialization():
    tree = [(97, '0'), (98, '10'), (99, '11')]  # Tree for (ASCII) 'a', 'b', 'c' + codes
    serialized = serialize_huffman_tree(tree)
    deserialized = deserialize_huffman_tree(serialized)
    assert deserialized == tree, "Huffman tree serialization/deserialization failed"

# Check if size reduction calculation works
def test_size_reduction(sample_data):
    enc_data, _, _ = huff_encode(sample_data)
    reduction = size_reduction(sample_data, enc_data)
    assert 0 <= reduction <= 100, "Invalid size reduction percentage"

# Test performance on large files
def test_large_file_performance(large_data):
    # Time Huffman compression
    start = time()
    enc_data, huff_c, padding = huff_encode(large_data)
    huffman_time = time() - start
    assert huff_decode(enc_data, huff_c, padding) == large_data, "Huffman failed on large data"
    
    # Time LZW compression
    start = time()
    comp_data, _ = lzw_encode(large_data)
    lzw_time = time() - start
    assert lzw_decode(comp_data) == large_data, "LZW failed on large data"
    
    print(f'Compression times - Huffman: {huffman_time:.4f}s, LZW: {lzw_time:.4f}s')

# LZW with small dictionary size
def test_max_dict_size():
    data = b'abcdefghijklmnopqrstuvwxyz' * 1000
    comp_data, _ = lzw_encode(data, max_dict_size=30)
    assert lzw_decode(comp_data, max_dict_size=30) == data, "LZW failed with limited dictionary"

# Testing different file sizes
@pytest.mark.parametrize('size', [2, 1024, 1024*1024])
def test_various_file_sizes(tmp_path, size):
    data = os.urandom(size)
    file_path = tmp_path / f"test_{size}.bin"
    write_file(str(file_path), data)
    
    read_data = read_file(str(file_path))
    assert len(read_data) == size and read_data == data, f"File I/O failed for {size} bytes"

# Error handling
def test_error_handling():
    # Raise an error because 65536 is not a valid LZW code
    with pytest.raises(ValueError, match="Bad compressed code: 65536"):
        lzw_decode([65536])

    # Raise an error because 300 is not in the initial LZW dictionary
    with pytest.raises(ValueError, match="Bad compressed code: 300"):
        lzw_decode([0, 300])

    # Raise a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        read_file("doesnt_exist.txt")

if __name__ == "__main__":
    pytest.main()