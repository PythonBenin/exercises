from random import randint, choice
from string import digits as ascii_digits, ascii_uppercase, ascii_lowercase, ascii_letters
from itertools import groupby, islice


digits = ascii_digits + ascii_uppercase + ascii_lowercase
max_run_length = len(digits) - 1


def batched(iterable, n, *, strict=False):
    """Available in Python 3.12"""
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch


def to_int(d: str):
    if d.isdigit():
        return ord(d) - ord('0')
    elif d.isupper():
        return 10 + ord(d) - ord('A')
    elif d.islower():
        return 36 + ord(d) - ord('a')
    else:
        raise Exception(f'Invalid base 62 digit: {d}')


def ilen(iterator):
    return sum(1 for _ in iterator)


def generate_rle_suitable_strings(n=50, min_len=10_000, max_len=100_000):
    """Based on a code provided by ChatGPT"""
    rle_suitable_strings = []

    for _ in range(n):
        length = randint(min_len, max_len)
        builder = []
        while len(builder) < length:
            ch = choice(ascii_letters)
            count = randint(1, 1000)
            builder.extend([ch] * count)
        s = ''.join(builder[:length])
        rle_suitable_strings.append(s)

    return rle_suitable_strings


def rle_encode(s):
    """Based on the function used in Wikipedia article on RLE"""
    builder = []
    for k, g in groupby(s):
        n = ilen(g)
        q, r = divmod(n, max_run_length)
        builder.extend([f'{digits[max_run_length]}{k}'] * q)
        if r != 0:
            builder.append(f'{digits[r]}{k}')

    return ''.join(builder)


def rle_decode(s):
    """Based on the function used in Wikipedia article on RLE"""
    builder = []
    for d, ch in batched(s, 2):
        n = to_int(d)
        builder.append(ch * n)

    return ''.join(builder)


for g in generate_rle_suitable_strings():
    ch, s = ('E', g) if randint(1, 100) % 2 == 0 else ('D', rle_encode(g))
    print(f'{ch} {s}')
