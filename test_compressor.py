import pytest
from compressor import read_file, huff_encode, huff_decode, lzw_encode, lzw_decode, size_red

# Test for reading files
def test_read_file():
    data = read_file('testtext.txt')
    assert data == read_file('text.txt')

# Test Huffman encoding and decoding with a simple message
def test_huff_encode_decode():
    data = read_file('testtext.txt')
    enc_data, huff_c = huff_encode(data)
    assert isinstance(enc_data, bytes)
    assert isinstance(huff_c, list)
    assert huff_decode(enc_data, huff_c) == data

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
