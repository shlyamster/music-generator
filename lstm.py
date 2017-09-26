# -*- coding: utf-8 -*-
import json
# import numpy
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import Dropout
# from keras.layers import LSTM
# from keras.callbacks import ModelCheckpoint
# from keras.utils import np_utils

import rutermextract

term_extractor = rutermextract.TermExtractor()


def terms(text):
    return [str(term.normalized) for term in term_extractor(text)]


if __name__ == '__main__':
    with open('texts.json', 'r') as json_file:
        texts = json.loads(json_file.read())

    super_text = ''
    for k, v in texts.items():
        super_text += v + '\n'

    del texts

    print(len(super_text))
    terms = term_extractor(super_text)
    print(len(terms))
    for term in terms[:40:]:
        print(term.normalized, term.count)
