import argparse
import json
import sys
 
from sources.hack import CaesarHacker
from sources.train import Trainer
from sources.encode import CaesarEncoderAndDecoder, VigenereEncoderAndDecoder, VernamEncoderAndDecoder
 

def code(args, decrypt):
    if args.cipher == 'caesar':
        encoder = CaesarEncoderAndDecoder(args.key)
    elif args.cipher == 'vigenere':
        encoder = VigenereEncoderAndDecoder(args.key)
    else:
        encoder = VernamEncoderAndDecoder(args.key)
    text = args.input_file.read()
    args.output_file.write(encoder.encode(text, decrypt))


def encode(args):
    code(args, False)
 
 
def decode(args):
    code(args, True)
 
 
def train(args):
    text = args.text_file.read()
    trainer = Trainer()
    trainer.feed(text)
    args.model_file.write(trainer.get_json_model())
 
 
def hack(args):
    try:
        model = json.load(args.model_file)
    except json.JSONDecodeError:
        raise SyntaxError('Model file is not correct')
    hacker = CaesarHacker(model)
    text = args.input_file.read()
    args.output_file.write(hacker.hack(text))
 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # parser to encode
    parser_encode = subparsers.add_parser('encode')
    parser_encode.add_argument('--cipher', choices=['caesar', 'vigenere', 'vernam'], required=True)
    parser_encode.add_argument('--key', required=True)
    parser_encode.add_argument('--input-file', type=argparse.FileType('r'), default=sys.stdin)
    parser_encode.add_argument('--output-file', type=argparse.FileType('w'), default=sys.stdout)
    parser_encode.set_defaults(func=encode)

    # parser to decode
    parser_decode = subparsers.add_parser('decode')
    parser_decode.add_argument('--cipher', choices=['caesar', 'vigenere', 'vernam'], required=True)
    parser_decode.add_argument('--key', required=True)
    parser_decode.add_argument('--input-file', type=argparse.FileType('r'), default=sys.stdin)
    parser_decode.add_argument('--output-file', type=argparse.FileType('w'),default=sys.stdout)
    parser_decode.set_defaults(func=decode)

    # parser to train
    parser_train = subparsers.add_parser('train')
    parser_train.add_argument('--text-file', type=argparse.FileType('r'), default=sys.stdin)
    parser_train.add_argument('--model-file', type=argparse.FileType('w'), required=True)
    parser_train.set_defaults(func=train)

    # parser to hack
    parser_hack = subparsers.add_parser('hack')
    parser_hack.add_argument('--input-file', type=argparse.FileType('r'), default=sys.stdin)
    parser_hack.add_argument('--output-file', type=argparse.FileType('w'), default=sys.stdout)
    parser_hack.add_argument('--model-file', type=argparse.FileType('r'), required=True)
    parser_hack.set_defaults(func=hack)

    args = parser.parse_args()
    args.func(args)

