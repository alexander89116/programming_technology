import pytest
from main import *
from train import *


class myArgs:
    def __init__(self, method='encode', cipher='caesar', key=12, input_file=sys.stdin, output_file=sys.stdout):
        self.method=method
        self.cipher = cipher
        self.key = key
        self.input_file = input_file
        self.output_file = output_file

def test_argument_cheker1():
    args = myArgs('encode', 'caesar', '12a')
    with pytest.raises(KeyError):
        argument_cheker(args)

def test_argument_cheker2():
    args = myArgs('decode', 'vigenere', '12a')
    with pytest.raises(KeyError):
        argument_cheker(args)

def test_caesar():
    a = caesar(12, 'techprog')
    b = caesar(-12, a)
    assert b == 'techprog'

def test_vigenere():
    a = vigenere('LEMON', 'techprogisthebestcourseever', 1)
    b = vigenere('LEMON', a, -1)
    assert b == 'techprogisthebestcourseever'