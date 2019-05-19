import pytest
from main import *
from train import *


class myArgs:
    def __init__(self, method='encode', cipher='caesar', key=12, input_file=sys.stdin, output_file=sys.stdout):
        self.method = method
        self.cipher = cipher
        self.key = key
        self.input_file = input_file
        self.output_file = output_file


def test_big_caesar():
    args = myArgs('encode', 'caesar', 10000, input_file=open('test_files/big_text.txt', 'r', encoding='utf-8'),
                  output_file=open('test_files/ans.txt', 'w', encoding='utf-8'))
    encode(args)
    assert caesar(10000, open('test_files/big_text.txt', 'r', encoding='utf-8').read()) == open('test_files/ans.txt', 'r', encoding='utf-8').read()


def test_small_caesar():
    args = myArgs('encode', 'caesar', 10000, input_file=open('test_files/small_text.txt', 'r', encoding='utf-8'),
                  output_file=open('test_files/ans.txt', 'w', encoding='utf-8'))
    encode(args)
    assert caesar(10000, open('test_files/small_text.txt', 'r', encoding='utf-8').read()) == open('test_files/ans.txt', 'r', encoding='utf-8').read()


def test_big_vigenere():
    args = myArgs('encode', 'vigenere', 'l', input_file=open('test_files/big_text.txt', 'r', encoding='utf-8'),
                  output_file=open('test_files/ans.txt', 'w', encoding='utf-8'))
    encode(args)
    assert vigenere('l', open('test_files/big_text.txt', 'r', encoding='utf-8').read(), 1) == open('test_files/ans.txt', 'r', encoding='utf-8').read()


def test_small_vigenere():
    args = myArgs('encode', 'vigenere', 'lemon', input_file=open('test_files/small_text.txt', 'r', encoding='utf-8'),
                  output_file=open('test_files/ans.txt', 'w', encoding='utf-8'))
    encode(args)
    assert vigenere('lemon', open('test_files/small_text.txt', 'r', encoding='utf-8').read(), 1) == open('test_files/ans.txt', 'r', encoding='utf-8').read()

test_big_caesar()
test_small_caesar()
test_big_vigenere()
test_small_vigenere()