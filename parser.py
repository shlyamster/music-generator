# -*- coding: utf-8 -*-
import json
import query

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
        'https://text-lyrics.ru/c1/slavakpss/'
    ]

    texts = dict()
    for index, artist in enumerate(artists):
        print('{}/{} - {}'.format(index + 1, len(artists), artist.split('/')[-2]))
        compositions = query.compositions(artist)
        compositions_texts = query.all_texts(compositions)
        texts.update(compositions_texts)

    json_texts = json.dumps(texts, indent=4, sort_keys=True)
    with open('texts.json', 'w') as json_file:
        json_file.write(json_texts)
