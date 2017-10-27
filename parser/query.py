# -*- coding: utf-8 -*-
from multiprocessing.pool import Pool
from .text_lyrics_query import TextLyricsQuery

query = TextLyricsQuery()


def parse_artist(artist: str) -> {str: str}:
    artist_compositions = query.compositions(artist)
    artist_texts = query.all_texts(artist_compositions)
    print(artist)
    return artist_texts


def parse_artists(artists: [str]) -> {str: str}:
    texts = {}
    for artist_texts in Pool(processes=20).map(parse_artist, artists):
        for key, value in artist_texts.items():
            if value not in texts.values():
                texts[key] = value
    return texts
