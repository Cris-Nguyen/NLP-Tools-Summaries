### Module imports ###
import time
import argparse
from utils import VnAnnotator, read_txt


### Global Variables ###
text_path = 'vi_text.txt'


### Class declarations ###


### Function declarations ###
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--lib', type=str, default='', required=True)
    parser.add_argument('--mode', type=str, default='', required=True)
    args = parser.parse_args()

    annotator = VnAnnotator()
    text_list = read_txt(text_path)
    output = f'{args.lib}/{args.mode}_{args.lib}_output.txt'
    t = time.time()
    annotator.annotate(args.lib, text_list, args.mode, output)
    print(time.time() - t)
