### Module imports ###
import time
import argparse
from underthesea import sent_tokenize, word_tokenize, pos_tag, chunk, ner, classify, sentiment
from vncorenlp import VnCoreNLP


### Global Variables ###


### Class declarations ###
class ViAnnotator:

    def underthesea_annotate(self, text, mode):
        if mode == 'sent_tokenize':
            return sent_tokenize(text)
        elif mode == 'word_tokenize':
            return word_tokenize(text)
        elif mode == 'pos_tag':
            return pos_tag(text)
        elif mode == 'chunk':
            return chunk(text)
        elif mode == 'ner':
            return ner(text)
        elif mode == 'classify':
            return classify(text)
        elif mode == 'sentiment':
            return sentiment(text)
        else:
            raise Exception("Wrong request, please check your request")

    def vncorenlp_annotate(self, vncorenlp_class, text, mode):
        if mode == 'word_tokenize':
            return vncorenlp_class.tokenize(text)
        elif mode == 'pos_tag':
            return vncorenlp_class.pos_tag(text)
        elif mode == 'ner':
            return vncorenlp_class.ner(text)
        elif mode == 'dep_parse':
            return vncorenlp_class.dep_parse(text)
        else:
            raise Exception("Wrong request, please check your request")

    def annotate(self, lib, text_list, mode, output):
        f = open(output, 'w')
        if lib == 'underthesea':
            t = time.time()
            count = 0
            for text in text_list:
                f.write(f'{text}\t{self.underthesea_annotate(text, mode)}\n')
                count += 1
                if time.time() - t > 1:
                    break
            print(count)

        elif lib == 'vncorenlp':
            vncorenlp_file = r'VnCoreNLP_lib/VnCoreNLP-1.1.1.jar'
            with VnCoreNLP(vncorenlp_file) as vncorenlp_class:
                t = time.time()
                count = 0
                for text in text_list:
                    f.write(f'{text}\t{self.vncorenlp_annotate(vncorenlp_class, text, mode)}\n')
                    count += 1
                    if time.time() - t > 1:
                        break
            print(count)

        else:
            raise Exception("Wrong request, please check your request")
        f.close()


### Function declarations ###
def read_txt(text_file):
    f = open(text_file, 'r')
    lines = f.readlines()
    text_list = []
    for line in lines:
        text_list.append(line[:-1])
    return text_list
