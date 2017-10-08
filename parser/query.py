# -*- coding: utf-8 -*-
from .text_lyrics_query import TextLyricsQuery


query = TextLyricsQuery()


def parse_artists(artists: [str]) -> {str: str}:
    texts = {}
    for index, artist in enumerate(artists):
        print('{}/{} - {}'.format(index + 1, len(artists), artist))
        artist_compositions = query.compositions(artist)
        artist_texts = query.all_texts(artist_compositions)
        for key, value in artist_texts.items():
            if value not in texts.values():
                texts[key] = value
    return texts
