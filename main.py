import string
import sys

len_ascii_lowercase = len(string.ascii_lowercase)

def argument_cheker(args):
    if args.method == 'encode' or args.method == 'decode':
        if args.cipher == 'caesar':
            if not args.key.isdigit():
                raise KeyError('Bad key format')
            args.key = int(args.key)
        elif args.cipher == 'vigenere':
            if not args.key.isalpha():
                raise KeyError('Bad key format')
            args.key = args.key.lower()

def encode(args):
    text = args.input_file.read()
    args.input_file.close()
    if args.cipher == 'caesar':
        encoder = caesar(args.key, text)
    else:
        encoder = vigenere(args.key, text, 1)
    args.output_file.write(encoder) 
    args.output_file.close()
    return 0


def decode(args):
    if args.cipher == 'caesar':
        args.key = -args.key
        return encode(args)
    else:
        text = args.input_file.read()
        decoder = vigenere(args.key, text, -1)
        args.output_file.write(decoder)


def caesar_calc(symbol: str, key: int):
    if symbol.isupper():
        code_a = ord('A')
    else:
        code_a = ord('a')
    return chr(code_a + (ord(symbol) - code_a + (len_ascii_lowercase + key) % len_ascii_lowercase) % len_ascii_lowercase)


def vigenere_calc(symbol: str, key: str, position: int, isEncoder: int):
    if symbol.isupper():
        code_a = ord('A')
    else:
        code_a = ord('a')
    return chr(code_a + (ord(symbol) + len_ascii_lowercase - code_a + isEncoder*(-ord('a') + ord(key[position % len(key)]))) % len_ascii_lowercase)


def vigenere(key: str, text: str, isEncoder: int):
    result = []
    position = 0
    for symbol in text:
        if symbol.isalpha():
            result.append(vigenere_calc(symbol, key, position, isEncoder))
            position += 1
        else:
            result.append(symbol)
    return ''.join(result)


def caesar(key: int, text: str):
    key = key % len_ascii_lowercase
    result = []
    for symbol in text:
        if symbol.isalpha():
            result.append(caesar_calc(symbol, key))
        else:
            result.append(symbol)
    return ''.join(result)
