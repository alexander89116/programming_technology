import argparse
import sys
import string

from main import argument_cheker, encode, decode
from train import train, hack

parser = argparse.ArgumentParser()
subs = parser.add_subparsers()

# encode
encode_parser = subs.add_parser('encode', description='Encode text')
encode_parser.set_defaults(method='encode')
encode_parser.add_argument('--cipher', choices=['caesar', 'vigenere'],
                           required=True, help='Cipher type')
encode_parser.add_argument('--key', required=True, help='Cipher key')
encode_parser.add_argument('--input-file', type=argparse.FileType('r', encoding='utf-8'), 
                            default=sys.stdin, help='Input file')
encode_parser.add_argument('--output-file', type=argparse.FileType('w', encoding='utf-8'),
                            default=sys.stdout, help='Output file')

# decode
decode_parser = subs.add_parser('decode', description='Decode text')
decode_parser.set_defaults(method='decode')
decode_parser.add_argument('--cipher', choices=['caesar', 'vigenere'],
                           required=True, help='Cipher type')
decode_parser.add_argument('--key', required=True, help='Cipher key')
decode_parser.add_argument('--input-file', type=argparse.FileType('r', encoding='utf-8'), 
                            default=sys.stdin, help='Input file')
decode_parser.add_argument('--output-file', type=argparse.FileType('w', encoding='utf-8'),
                            default=sys.stdout, help='Output file')

# train
train_parser = subs.add_parser('train', description='Train program')
train_parser.set_defaults(method='train')
train_parser.add_argument('--text-file',  type=argparse.FileType('r', encoding='utf-8'),
                          default=sys.stdin, help='Text file')
train_parser.add_argument('--model-file', type=argparse.FileType('w', encoding='utf-8'),
                          required=True, help='Model file')

# hack
hack_parser = subs.add_parser('hack', description='Hack cipher')
hack_parser.set_defaults(method='hack')
hack_parser.add_argument('--input-file', type=argparse.FileType('r', encoding='utf-8'),  
                            default=sys.stdin, help='Input file')
hack_parser.add_argument('--output-file', type=argparse.FileType('w', encoding='utf-8'),
                            default=sys.stdout, help='Output file')
hack_parser.add_argument('--model-file', type=argparse.FileType('r', encoding='utf-8'), required=True, help='Model file')

args = parser.parse_args()

argument_cheker(args)

if args.method == 'encode':
    encode(args)
elif args.method == 'decode':
    decode(args)
elif args.method == 'train':
    train(args)
elif args.method == 'hack':
    hack(args)
