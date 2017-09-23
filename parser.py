# -*- coding: utf-8 -*-
import json
import query

if __name__ == '__main__':
    # artists = query.artists('t')
    # artist = artists.get('Thomas Mraz')

    compositions = query.compositions('Thomas Mraz')

    # print(query.text('https://text-lyrics.ru/t/thomas-mraz/6232-thomas-mraz-manevrirovat-text-pesni.html'))
    # print(query.text('https://text-lyrics.ru/o/oxxxymiron/8398-oxxxymiron-bipolyarochka-text-pesni.html'))

    texts = query.all_texts(compositions)
    for k, v in texts.items():
        print('------------------------------------------------')
        print(k)
        print(v)

    # print(json.dumps(, indent=4, sort_keys=True))
