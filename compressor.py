import heapq as hq
import time
import pickle
from collections import defaultdict as ddict

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def huff_encode(msg):
    freqs = ddict(int)
    for c in msg:
        freqs[c] += 1

    pq = [[w, [sym, ""]] for sym, w in freqs.items()]
    hq.heapify(pq)

    while len(pq) > 1:
        lo = hq.heappop(pq)
        hi = hq.heappop(pq)
        for p in lo[1:]:
            p[1] = '0' + p[1]
        for p in hi[1:]:
            p[1] = '1' + p[1]
        hq.heappush(pq, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huff_c = sorted(hq.heappop(pq)[1:], key=lambda p: (len(p[-1]), p))

    enc_msg = ""
    for c in msg:
        for item in huff_c:
            if c == item[0]:
                enc_msg += item[1]
                break

    # Padding enc_msg to ensure it contains a multiple of 8 bits
    extra_padding = 8 - len(enc_msg) % 8
    enc_msg += '0' * extra_padding

    # Converting bit string to bytes
    enc_msg = int(enc_msg, 2).to_bytes((len(enc_msg) + 7) // 8, byteorder='big')

    return enc_msg, huff_c, extra_padding

def huff_decode(enc_msg, huff_c, extra_padding):
    inv_huff_c = {i[1]: i[0] for i in huff_c}

    # Converting bytes to bit string
    enc_msg = bin(int.from_bytes(enc_msg, byteorder='big'))[2:]
    enc_msg = enc_msg[0: len(enc_msg) - extra_padding]

    dec_msg = b""
    t = ""
    for d in enc_msg:
        t += d
        if t in inv_huff_c:
            dec_msg += bytes([inv_huff_c[t]])
            t = ""
    return dec_msg

def lzw_encode(msg):
    dict_size = 256
    dict_ = {bytes([i]): i for i in range(dict_size)}
    s = bytes([msg[0]])
    res = []
    for char in msg[1:]:
        char = bytes([char])
        s_plus_char = s + char
        if s_plus_char in dict_:
            s = s_plus_char
        else:
            res.append(dict_[s])
            dict_[s_plus_char] = dict_size
            dict_size += 1
            s = char
    res.append(dict_[s])
    return res, dict_

def lzw_decode(comp_msg, dict_):
    inv_dict = {v: k for k, v in dict_.items()}

    dec_msg = inv_dict[comp_msg[0]]
    s = dec_msg
    for k in comp_msg[1:]:
        if k in inv_dict:
            ent = inv_dict[k]
        elif k == len(inv_dict):
            ent = s + s[0:1]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        dec_msg += ent
        inv_dict[len(inv_dict)] = s + ent[0:1]
        s = ent
    return dec_msg

def size_red(orig, comp):
    orig_s = len(orig)
    comp_s = len(comp)
    red = (orig_s - comp_s) / orig_s * 100
    return red

def check(file_path):
    print(f"Conducting compression...")
    tst_msg = read_file(file_path)

    start_time = time.time()
    h_enc_msg, h_codes, extra_padding = huff_encode(tst_msg) # Catch extra_padding
    huffman_time = time.time() - start_time
    h_dec_msg = huff_decode(h_enc_msg, h_codes, extra_padding) # Pass extra_padding
    if tst_msg == h_dec_msg:
        print("Huffman: Compressed equals the original one.")
        write_file('packedHuff/compressed.bin', h_enc_msg)
    else:
        print("Huffman decoding failed!")
    h_red = size_red(tst_msg, h_enc_msg)
    print(f"Huffman reduced the size by {h_red}%")
    print(f"Huffman compression took {huffman_time} seconds.")

    start_time = time.time()
    lzw_comp_msg, lzw_dict = lzw_encode(tst_msg)
    lzw_time = time.time() - start_time
    lzw_dec_msg = lzw_decode(lzw_comp_msg, lzw_dict)
    if tst_msg == lzw_dec_msg:
        print("LZW: Compressed equals the original one.")
        write_file('packedLZW/compressed.bin', lzw_comp_msg)
    else:
        print("LZW decoding failed!")
    lzw_red = size_red(tst_msg, ''.join(map(str,lzw_comp_msg)))
    print(f"LZW reduced the size by {lzw_red}%")
    print(f"LZW compression took {lzw_time} seconds.")

    print("Passed all tests!")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 compressor.py binary_file_path")
    else:
        check(sys.argv[1])
