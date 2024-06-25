import heapq as hq
from time import time
from collections import defaultdict
from os import path
from typing import Tuple, List, Dict, Union
from .config import BASE_PATH
import pickle
import struct

def read_file(file_path: str, size: int = None) -> bytes:
    with open(file_path, 'rb') as file:
        return file.read(size)

def write_file(file_path: str, data: Union[bytes, List[int]]) -> None:
    with open(file_path, 'wb') as file:
        file.write(data)

# Huffman encoding function. Returns encoded bytes, Huffman codes, and padding length.
def huff_encode(input: bytes) -> Tuple[bytes, List[Tuple[int, str]], int]:
    if not input:
        return b'', [], 0

    # Count frequency of each byte
    freq_dict = defaultdict(int)
    for byte in input:
        freq_dict[byte] += 1

    # Create a min heap of nodes. Each node is [weight, [symbol, code]]
    heap = [[weight, [symbol, ""]] for symbol, weight in freq_dict.items()]
    hq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        low = hq.heappop(heap)
        high = hq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        hq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    # Generate Huffman codes
    huffman_codes = sorted(hq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    code_dict = {symbol: code for symbol, code in huffman_codes}

    # Encode the input
    encoded_str = ''.join(code_dict[byte] for byte in input)
    padding_length = 8 - len(encoded_str) % 8
    encoded_str += '0' * padding_length

    # Convert binary string to bytes
    encoded_bytes = int(encoded_str, 2).to_bytes((len(encoded_str) + 7) // 8, byteorder='big')

    return encoded_bytes, huffman_codes, padding_length

# Huffman decoding function. Takes encoded bytes, Huffman codes, and padding length.
def huff_decode(encoded_bytes: bytes, huffman_codes: List[Tuple[int, str]], padding_length: int) -> bytes:
    if not encoded_bytes or not huffman_codes:
        return b''

    # Reverse the Huffman codes for decoding
    inverse_codes = {code: symbol for symbol, code in huffman_codes}
    
    # Convert bytes to binary string and remove padding
    binary_str = bin(int.from_bytes(encoded_bytes, byteorder='big'))[2:].zfill(len(encoded_bytes) * 8)
    binary_str = binary_str[:-padding_length]

    # Decode the binary string
    decoded_input = bytearray()
    temp_code = ""
    for bit in binary_str:
        temp_code += bit
        if temp_code in inverse_codes:
            decoded_input.append(inverse_codes[temp_code])
            temp_code = ""

    return bytes(decoded_input)

# Serialize the Huffman tree for storage
def serialize_huffman_tree(tree: List[Tuple[int, str]]) -> bytes:
    return pickle.dumps(tree)

# Deserialize the Huffman tree from storage
def deserialize_huffman_tree(serialized_tree: bytes) -> List[Tuple[int, str]]:
    return pickle.loads(serialized_tree)

# Write Huffman compressed data to a file
def write_huffman_compressed(file_path: str, encoded_bytes: bytes, huffman_codes: List[Tuple[int, str]], padding_length: int) -> None:
    serialized_tree = serialize_huffman_tree(huffman_codes)
    tree_size = len(serialized_tree)
    
    with open(file_path, 'wb') as file:
        # Write tree size (4 bytes), padding length (1 byte), tree data, and encoded data
        file.write(struct.pack('>I', tree_size))
        file.write(struct.pack('B', padding_length))
        file.write(serialized_tree)
        file.write(encoded_bytes)

# Read Huffman compressed data from a file
def read_huffman_compressed(file_path: str) -> Tuple[bytes, List[Tuple[int, str]], int]:
    with open(file_path, 'rb') as file:
        tree_size = struct.unpack('>I', file.read(4))[0]
        padding_length = struct.unpack('B', file.read(1))[0]
        serialized_tree = file.read(tree_size)
        encoded_bytes = file.read()
    
    huffman_codes = deserialize_huffman_tree(serialized_tree)
    return encoded_bytes, huffman_codes, padding_length

# LZW encoding function. Returns encoded data and final dictionary.
def lzw_encode(input_data: bytes, max_dict_size: int = 6000) -> Tuple[List[int], Dict[bytes, int]]:
    if not input_data:
        return [], {}

    # Initialize dictionary with single-byte sequences
    dict_size = 256
    dictionary = {bytes([i]): i for i in range(dict_size)}
    result = []
    atm = bytes([input_data[0]])
    # LZW compression loop
    for bte in input_data[1:]:
        bte = bytes([bte])
        new = atm + bte
        if new in dictionary:
            atm = new
        else:
            result.append(dictionary[atm])
            if len(dictionary) < max_dict_size:
                dictionary[new] = dict_size
                dict_size += 1
            atm = bte
    
    # Output code for remaining sequence
    if atm:
        result.append(dictionary[atm])
    
    return result, dictionary

# LZW decoding function. Takes encoded data and max dictionary size.
def lzw_decode(encoded_input: List[int], max_dict_size: int = 6000) -> bytes:
    if not encoded_input:
        return b''

    # Initialize dictionary with single-byte sequences
    dict_size = 256
    dictionary = {i: bytes([i]) for i in range(dict_size)}
    
    result = bytearray()
    
    # Handle the first code
    if encoded_input[0] >= dict_size:
        raise ValueError(f'Bad compressed code: {encoded_input[0]}')
    atm = dictionary[encoded_input[0]]
    result.extend(atm)
    
    # LZW decompression loop
    for code in encoded_input[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == dict_size:
            entry = atm + atm[:1]
        else:
            raise ValueError(f'Bad compressed code: {code}')
        
        result.extend(entry)
        
        if len(dictionary) < max_dict_size:
            dictionary[dict_size]= atm + entry[:1]
            dict_size += 1
        
        atm=entry
    
    return bytes(result)

# Write LZW compressed data to a file
def write_compressed_to_file(comp_msg: List[int], file_path: str) -> None:
    with open(file_path, 'wb') as f:
        for code in comp_msg:
            f.write(code.to_bytes(2,byteorder='big'))

# Read LZW compressed data from a file
def read_compressed_from_file(file_path: str) -> List[int]:
    with open(file_path, 'rb') as f:
        byte_data = f.read()
    return [int.from_bytes(byte_data[i:i+2], byteorder='big') for i in range(0, len(byte_data), 2)]

# Calculate size reduction percentage
def size_reduction(original: bytes, compressed: bytes) -> float:
    return len(compressed) / len(original) * 100

# Print and write compression results
def print_compression_results(method: str, original: bytes, compressed: bytes, time_taken: float, file, additional_size: int = 0) -> None:
    compressed_size = len(compressed) + additional_size
    reduction = compressed_size / len(original) * 100
    result_str = f"{method} compression is {reduction:.2f}% of the original size.\n{method} compression took {time_taken:.4f} seconds.\n"
    print(result_str)
    file.write(result_str)

# Main function to check compression
def check(file_path: str) -> None:
    MAX_SIZE = 1024 * 1024 * 20  # 20 MB
    size = 2
    results_file = path.join(BASE_PATH, 'results.txt')

    with open(results_file, 'w') as file:
        while size < MAX_SIZE:
            tst_msg = read_file(file_path, size)
            print(f"Compressing {len(tst_msg)} bytes ({len(tst_msg) / 1024:.2f} KB, {len(tst_msg) / 1024 / 1024:.2f} MB)")
            file.write(f"Compressing {len(tst_msg)} bytes ({len(tst_msg) / 1024:.2f} KB, {len(tst_msg) / 1024 / 1024:.2f} MB)\n")

            # Huffman compression
            start_time = time()
            h_enc_msg, h_codes, extra_padding = huff_encode(tst_msg)
            huffman_time = time() - start_time

            huffman_compressed_path = path.join(BASE_PATH, 'packedHuff/compressed.bin')
            write_huffman_compressed(huffman_compressed_path, h_enc_msg, h_codes, extra_padding)

            # Verify Huffman compression
            read_enc_msg, read_codes, read_padding = read_huffman_compressed(huffman_compressed_path)

            h_dec_msg = huff_decode(read_enc_msg, read_codes, read_padding)
            if tst_msg == h_dec_msg:
                print("Huffman decoding successful!")
                text_file_path = path.join(BASE_PATH, 'packedHuff/decoded.txt')
                with open(text_file_path, 'w') as txt_file:
                    txt_file.write(h_dec_msg.decode(errors='ignore'))

                compressed_size = path.getsize(huffman_compressed_path)
            else:
                raise ValueError("Huffman decoding failed!")

            print_compression_results("Huffman", tst_msg, h_enc_msg, huffman_time, file, additional_size=compressed_size - len(h_enc_msg))
            
            # LZW compression
            start_time = time()
            lzw_comp_msg, lzw_dict = lzw_encode(tst_msg, max_dict_size=6000)
            lzw_time = time() - start_time

            # Verify LZW compression
            lzw_dec_msg = lzw_decode(lzw_comp_msg, max_dict_size=6000)
            if tst_msg == lzw_dec_msg:
                print("LZW decoding successful!")
                write_compressed_to_file(lzw_comp_msg, path.join(BASE_PATH, 'packedLZW/compressed.bin'))

                text_file_path = path.join(BASE_PATH, 'packedLZW/decoded.txt')
                with open(text_file_path, 'w') as txt_file:
                    txt_file.write(lzw_dec_msg.decode(errors='ignore'))
            else:
                raise ValueError("LZW decoding failed!")

            with open(path.join(BASE_PATH, 'packedLZW/compressed.bin'), 'rb') as f:
                lzw_comp_bytes = f.read()

            print_compression_results("LZW", tst_msg, lzw_comp_bytes, lzw_time, file)

            file.write('\n'+ '-'*10 +'\n')

            size *= 2