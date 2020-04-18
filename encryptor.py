import argparse
import json
import sys
 
from sources.hack import CaesarHacker
from sources.train import Trainer
from sources.encode import CaesarEncoderAndDecoder, VigenereEncoderAndDecoder
 
 
def encode(args):
    if args.cipher == 'caesar':
        encoder = CaesarEncoderAndDecoder(args.key)
    else:
        encoder = VigenereEncoderAndDecoder(args.key)
    if args.input_file:
        text = args.input_file.read()
    else:
        text = sys.stdin.read()
    if args.output_file:
        args.output_file.write(encoder.encode(text))
    else:
        sys.stdout.write(encoder.encode(text))
 
 
def decode(args):
    if args.cipher == 'caesar':
        decoder = CaesarEncoderAndDecoder(args.key)
    else:
        decoder = VigenereEncoderAndDecoder(args.key)
    if args.input_file:
        text = args.input_file.read()
    else:
        text = sys.stdin.read()
    if args.output_file:
        args.output_file.write(decoder.decode(text))
    else:
        sys.stdout.write(decoder.decode(text))
 
 
def train(args):
    if args.text_file:
        text = args.text_file.read()
    else:
        text = sys.stdin.read()
    trainer = Trainer()
    trainer.feed(text)
    args.model_file.write(trainer.get_json_model())
 
 
def hack(args):
    try:
        model = json.load(args.model_file)
    except json.JSONDecodeError:
        raise Exception('Model file is not correct')
    hacker = CaesarHacker(model)
    if args.input_file:
        text = args.input_file.read()
    else:
        text = sys.stdin.read()
    if args.output_file:
        args.output_file.write(hacker.hack(text))
    else:
        sys.stdout.write(hacker.hack(text))
 
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
 
    # parser to encode
    parser_encode = subparsers.add_parser('encode')
    parser_encode.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
    parser_encode.add_argument('--key', required=True)
    parser_encode.add_argument('--input-file', type=argparse.FileType('r'))
    parser_encode.add_argument('--output-file', type=argparse.FileType('w'))
    parser_encode.set_defaults(func=encode)
 
    # parser to decode
    parser_decode = subparsers.add_parser('decode')
    parser_decode.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
    parser_decode.add_argument('--key', required=True)
    parser_decode.add_argument('--input-file', type=argparse.FileType('r'))
    parser_decode.add_argument('--output-file', type=argparse.FileType('w'))
    parser_decode.set_defaults(func=decode)
 
    # parser to train
    parser_train = subparsers.add_parser('train')
    parser_train.add_argument('--text-file', type=argparse.FileType('r'))
    parser_train.add_argument('--model-file', type=argparse.FileType('w'), required=True)
    parser_train.set_defaults(func=train)
 
    # parser to hack
    parser_hack = subparsers.add_parser('hack')
    parser_hack.add_argument('--input-file', type=argparse.FileType('r'))
    parser_hack.add_argument('--output-file', type=argparse.FileType('w'))
    parser_hack.add_argument('--model-file', type=argparse.FileType('r'), required=True)
    parser_hack.set_defaults(func=hack)
 
    args = parser.parse_args()
    args.func(args)

