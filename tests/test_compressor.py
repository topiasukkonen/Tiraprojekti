import pytest
import os
import time
from compressor import read_file, huff_encode, huff_decode, lzw_encode, lzw_decode, size_red

# Test for reading files
def test_read_file():
    data = read_file('testtext.txt')
    assert data == read_file('testtext.txt')

# Test Huffman encoding and decoding with a simple message
def test_huff_encode_decode():
    data = read_file('testtext.txt')
    enc_data, huff_c, extra_padding = huff_encode(data)
    assert isinstance(enc_data, bytes)
    assert isinstance(huff_c, list)
    assert huff_decode(enc_data, huff_c, extra_padding) == data

# Test LZW encoding and decoding with a simple message
def test_lzw_encode_decode():
    data = read_file('testtext.txt')
    comp_data, lzw_dict = lzw_encode(data)
    assert isinstance(comp_data, list)
    assert isinstance(lzw_dict, dict)
    assert lzw_decode(comp_data, lzw_dict) == data

# Test size reduction
def test_size_red():
    orig = read_file('testtext.txt')
    comp = huff_encode(orig)[0]  # Compressed using Huffman encoding as an example
    assert isinstance(size_red(orig, comp), float)

# Test Huffman encoding and decoding with different types of data
@pytest.mark.parametrize('data', [
    b'This is ASCII text.',
    '这是一些Unicode文本'.encode('utf-8'),
    os.urandom(1024),
])
def test_huff_with_different_data(data):
    enc_data, huff_c, extra_padding = huff_encode(data)
    assert huff_decode(enc_data, huff_c, extra_padding) == data

# Test LZW encoding and decoding with different types of data
@pytest.mark.parametrize('data', [
    b'This is ASCII text.',
    '这是一些Unicode文本'.encode('utf-8'),
    os.urandom(1024),
])
def test_lzw_with_different_data(data):
    comp_data, lzw_dict = lzw_encode(data)
    assert lzw_decode(comp_data, lzw_dict) == data

# Test with empty input
def test_with_empty_input():
    data = b''
    enc_data, huff_c, extra_padding = huff_encode(data)
    assert huff_decode(enc_data, huff_c, extra_padding) == data
    comp_data, lzw_dict = lzw_encode(data)
    assert lzw_decode(comp_data, lzw_dict) == data

# Test with large files
def test_with_large_files():
    data = os.urandom(1024 * 1024 * 5)  # 5 MB
    start = time.time()
    enc_data, huff_c, extra_padding = huff_encode(data)
    assert huff_decode(enc_data, huff_c, extra_padding) == data
    print(f'Huffman compression and decompression of 5 MB took {time.time() - start} seconds')
    start = time.time()
    comp_data, lzw_dict = lzw_encode(data)
    assert lzw_decode(comp_data, lzw_dict) == data
    print(f'LZW compression and decompression of 5 MB took {time.time() - start} seconds')

# Test if the compressed size is smaller than the original size
def test_compressed_size():
    data = read_file('testtext.txt')
    huff_comp = huff_encode(data)[0]
    lzw_comp = ''.join(map(str, lzw_encode(data)[0]))
    assert len(huff_comp) < len(data)
    assert len(lzw_comp) < len(data)
