# -*- coding: utf-8 -*-
import os
import json
import parser


def save_texts(texts, filename):
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, 'wb') as json_file:
        json_file.write(json.dumps(texts, indent=4, sort_keys=True).encode('UTF-8'))


if __name__ == '__main__':
    artists = [
        'https://text-lyrics.ru/x1/haski/',
        'https://text-lyrics.ru/y/yanix/',
        'https://text-lyrics.ru/a/atl/',
        'https://text-lyrics.ru/l1/lsl/',
        'https://text-lyrics.ru/l1/luperkal/',
        'https://text-lyrics.ru/p/pharaoh/',
        'https://text-lyrics.ru/o/oxxxymiron/',
        'https://text-lyrics.ru/s/schokk/',
        'https://text-lyrics.ru/s/st/',
        'https://text-lyrics.ru/a/alphavite/',
        'https://text-lyrics.ru/g/guf/',
        'https://text-lyrics.ru/s/slim/',
        'https://text-lyrics.ru/b1/basta/',
        'https://text-lyrics.ru/n1/noganno/',
        'https://text-lyrics.ru/o/obladaet/',
        'https://text-lyrics.ru/m/markul/',
        'https://text-lyrics.ru/k1/kasta/',
        'https://text-lyrics.ru/c1/slavakpss/',
        'https://text-lyrics.ru/j/jubilee/',
        'https://text-lyrics.ru/b/boulevard-depo/',
        'https://text-lyrics.ru/t/thomas-mraz/'
    ]

    texts = parser.parse_artists(artists)
    save_texts(texts, 'data/super_texts.json')
