import heapq as hq
from time import time
from collections import defaultdict
from os import path
from typing import Tuple, List, Dict, Union
from .config import BASE_PATH

def read_file(file_path: str, size: int = None) -> bytes:
    """Read n-bytes of binary data from a file.

    Args:
        file_path (str): Path to the file.
        size (int): Number of bytes to read.

    Returns:
        bytes: Content of the file.
    """
    with open(file_path, 'rb') as file:
        return file.read(size)

def write_file(file_path: str, data: Union[bytes, List[int]]) -> None:
    """Write binary data to a file.
a
    Args:
        file_path (str): Path to the file.
        data (Union[bytes, List[int]]): Data to write to the file.
    """
    with open(file_path, 'wb') as file:
        file.write(data)
        #pickle.dump(data, file)

def huff_encode(msg: bytes) -> Tuple[bytes, List[Tuple[int, str]], int]:
    """Encode a message using Huffman coding.

    Args:
        msg (bytes): The message to encode.

    Returns:
        Tuple[bytes, List[Tuple[int, str]], int]: Encoded message, Huffman codes, and extra padding length.
    """
    if not msg:
        return b'', [], 0

    freqs = defaultdict(int)
    for c in msg:
        freqs[c] += 1

    pq = [[weight, [sym, ""]] for sym, weight in freqs.items()]
    hq.heapify(pq)

    while len(pq) > 1:
        lo = hq.heappop(pq)
        hi = hq.heappop(pq)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        hq.heappush(pq, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huff_c = sorted(hq.heappop(pq)[1:], key=lambda p: (len(p[-1]), p))
    huff_dict = {symbol: code for symbol, code in huff_c}

    enc_msg = ''.join(huff_dict[c] for c in msg)

    extra_padding = 8 - len(enc_msg) % 8
    enc_msg += '0' * extra_padding

    enc_msg = int(enc_msg, 2).to_bytes((len(enc_msg) + 7) // 8, byteorder='big')

    return enc_msg, huff_c, extra_padding

def huff_decode(enc_msg: bytes, huff_c: List[Tuple[int, str]], extra_padding: int) -> bytes:
    """Decode a Huffman encoded message.

    Args:
        enc_msg (bytes): Encoded message.
        huff_c (List[Tuple[int, str]]): Huffman codes.
        extra_padding (int): Extra padding length.

    Returns:
        bytes: Decoded message.
    """
    if not enc_msg or not huff_c:
        return b''

    inv_huff_c = {code: symbol for symbol, code in huff_c}

    enc_msg = bin(int.from_bytes(enc_msg, byteorder='big'))[2:].zfill(len(enc_msg) * 8)
    enc_msg = enc_msg[:-extra_padding]

    dec_msg = bytearray()
    temp = ""
    for bit in enc_msg:
        temp += bit
        if temp in inv_huff_c:
            dec_msg.append(inv_huff_c[temp])
            temp = ""
    return bytes(dec_msg)

def lzw_encode(msg: bytes, max_dict_size: int = 4096) -> Tuple[List[int], Dict[bytes, int]]:
    """Encode a message using LZW compression with a capped dictionary size.

    Args:
        msg (bytes): The message to encode.
        max_dict_size (int): Maximum dictionary size.

    Returns:
        Tuple[List[int], Dict[bytes, int]]: Encoded message and dictionary used for encoding.
    """
    if not msg:
        return [], {}

    dict_size = 256
    dictionary = {bytes([i]): i for i in range(dict_size)}
    s = bytes([msg[0]])
    result = []
    for char in msg[1:]:
        char = bytes([char])
        s_plus_char = s + char
        if s_plus_char in dictionary:
            s = s_plus_char
        else:
            result.append(dictionary[s])
            if dict_size < max_dict_size:
                dictionary[s_plus_char] = dict_size
                dict_size += 1
            else:
                dictionary = {bytes([i]): i for i in range(256)}
                dict_size = 256
                dictionary[s_plus_char] = dict_size
                dict_size += 1
            s = char
    result.append(dictionary[s])
    return result, dictionary



def lzw_decode(comp_msg: List[int], max_dict_size: int = 4096) -> bytes:
    """Decode a LZW compressed message.

    Args:
        comp_msg (List[int]): Compressed message.
        max_dict_size (int): Maximum dictionary size.

    Returns:
        bytes: Decoded message.
    """
    if not comp_msg:
        return b''

    dict_size = 256
    inv_dict = {i: bytes([i]) for i in range(dict_size)}

    dec_msg = inv_dict[comp_msg[0]]
    s = dec_msg
    for k in comp_msg[1:]:
        if k in inv_dict:
            entry = inv_dict[k]
        elif k == len(inv_dict):
            entry = s + s[0:1]
        else:
            raise ValueError(f'Bad compressed k: {k}')
        dec_msg += entry
        if len(inv_dict) < max_dict_size:
            inv_dict[dict_size] = s + entry[0:1]
            dict_size += 1
        else:
            inv_dict = {i: bytes([i]) for i in range(256)}
            dict_size = 256
            inv_dict[dict_size] = s + entry[0:1]
            dict_size += 1
        s = entry
    return dec_msg



def write_compressed_to_file(comp_msg: List[int], file_path: str) -> None:
    """Write the compressed message to a binary file.

    Args:
        comp_msg (List[int]): Compressed message.
        file_path (str): Path to the file where compressed message will be written.
    """
    # Convert the list of codes to a bit string
    bit_string = ''.join(format(code, '012b') for code in comp_msg)
    byte_array = bytearray()

    # Convert the bit string to bytes
    for i in range(0, len(bit_string), 8):
        byte_array.append(int(bit_string[i:i+8], 2))

    with open(file_path, 'wb') as f:
        f.write(byte_array)

def read_compressed_from_file(file_path: str) -> List[int]:
    """Read the compressed message from a binary file.

    Args:
        file_path (str): Path to the file containing the compressed message.

    Returns:
        List[int]: Compressed message.
    """
    with open(file_path, 'rb') as f:
        byte_array = f.read()

    # Convert the bytes back to a bit string
    bit_string = ''.join(format(byte, '08b') for byte in byte_array)
    
    # Extract 12-bit codes from the bit string
    comp_msg = [int(bit_string[i:i+12], 2) for i in range(0, len(bit_string), 12) if i + 12 <= len(bit_string)]

    return comp_msg

def size_reduction(original: bytes, compressed: bytes) -> float:
    """Calculate the size reduction percentage.

    Args:
        original (bytes): Original message.
        compressed (bytes): Compressed message.

    Returns:
        float: Size reduction percentage.
    """
    return len(compressed) / len(original) * 100

def print_compression_results(method: str, original: bytes, compressed: bytes, time_taken: float, file) -> None:
    """Print and log the results of the compression method.

    Args:
        method (str): Compression method name.
        original (bytes): Original message.
        compressed (bytes): Compressed message.
        time_taken (float): Time taken for compression.
        file: File object to log the results.
    """
    reduction = size_reduction(original, compressed)
    result_str = f"{method} compression is {reduction:.2f}% of the original size.\n{method} compression took {time_taken:.4f} seconds.\n"
    print(result_str)
    file.write(result_str)
def check(file_path: str) -> None:
    """Conduct compression tests on a file.

    Args:
        file_path (str): Path to the file to be tested.
    """
    MAX_SIZE = 1024 * 1024 * 5  # 5 MB
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

            h_dec_msg = huff_decode(h_enc_msg, h_codes, extra_padding)
            if tst_msg == h_dec_msg:
                print("Huffman decoding successful!")
                write_file(path.join(BASE_PATH, 'packedHuff/compressed.bin'), h_enc_msg)
                text_file_path = path.join(BASE_PATH, 'packedHuff/decoded.txt')
                with open(text_file_path, 'w') as txt_file:
                    txt_file.write(h_dec_msg.decode(errors='ignore'))
            else:
                raise ValueError("Huffman decoding failed!")

            print_compression_results("Huffman", tst_msg, h_enc_msg, huffman_time, file)
            
            # LZW compression
            start_time = time()
            lzw_comp_msg, lzw_dict = lzw_encode(tst_msg)
            lzw_time = time() - start_time

            lzw_dec_msg = lzw_decode(lzw_comp_msg, max_dict_size=4096)
            if tst_msg == lzw_dec_msg:
                print("LZW decoding successful!")
                write_compressed_to_file(lzw_comp_msg, path.join(BASE_PATH, 'packedLZW/compressed.bin'))

                # Save the decoded LZW message to a text file
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
