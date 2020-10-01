### Module imports ###
import time
import argparse
import nltk
import spacy


### Global Variables ###


### Class declarations ###
class EnAnnotator:
    """ Annotator for processing English text """
    def nltk_annotate(self, text, mode):
        """ NLTK supports word segmentation, pos tagging and name entity recognition,
            It also supports dependency parsing but using StanfordCoreNLP features """
        if mode == 'word_tokenize':
            return nltk.word_tokenize(text)
        elif mode == 'pos_tag':
            return nltk.pos_tag(text)
        elif mode == 'ner':
            return nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text)))

    def spacy_annotate(self, spacy_nlp, text, mode):
        """ Spacy supports word segmentation, pos tagging and name entity recognition,
            dependency parsing """
        doc = spacy_nlp(text)
        if mode == 'word_tokenize':
            return [token.text for token in doc]
        elif mode == 'pos_tag':
            return [(token.text, token.pos) for token in doc]
        elif mode == 'ner':
            ner = []
            for ent in doc.ents:
                ner.append((ent.text, ent.label))
            return ner

        elif mode == 'dep_parse':
            dep_parse = []
            for chunk in doc.noun_chunks:
                dep_parse.append((chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text))
            return dep_parse

        else:
            raise Exception("Wrong request, please check your request")

    def annotate(self, lib, text_list, mode, output):
        f = open(output, 'w')
        if lib == 'nltk':
            t = time.time()
            count = 0
            for text in text_list:
                f.write(f'{text}\t{self.nltk_annotate(text, mode)}\n')
                count += 1
                # Check the sentences are processed in 1s
                if time.time() - t > 1:
                    break
            return count

        elif lib == 'spacy':
            spacy_nlp = spacy.load("en_core_web_sm")
            t = time.time()
            count = 0
            for text in text_list:
                f.write(f'{text}\t{self.spacy_annotate(spacy_nlp, text, mode)}\n')
                count += 1
                # Check the sentences are processed in 1s
                if time.time() - t > 1:
                    break
            return count

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
