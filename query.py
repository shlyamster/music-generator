# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

_site = 'text-lyrics.ru'
__alphabet = dict(zip('abcdefghijklmnopqrstuvwxyz1234567890абвгдеёжзиклмнопрстуфхцчшщэюя', list('abcdefghijklmnopqrstuvwxyz1234567890') + 'a1 b1 v1 g1 d1 e1 e1 gg z1 i1 k1 l1 m1 n1 o1 p1 r1 c1 t1 u1 f1 x1 z2 ch sh sh1 e2 yu i2'.split(' ')))


def artists(first_symbol):
    first_symbol = __alphabet.get(first_symbol.lower())
    url = 'https://{}/{}.html'.format(_site, first_symbol)
    response = requests.get(url, timeout=1)

    href = re.compile('^http://{}/{}/*'.format(_site, first_symbol))
    soup = BeautifulSoup(response.text, 'lxml').findAll('a', href=href)
    return {str(link.string): str(link.get('href')) for link in soup}


def compositions(artist):
    url = artist if artist.find(_site) != -1 else artists(str(artist[0])).get(artist)
    response = requests.get(url, timeout=1)
    url = url.replace('http', 'https')

    href = re.compile('^{}*'.format(url))
    soup = BeautifulSoup(response.text, 'lxml').findAll('a', href=href)

    result = {}
    for link in soup:
        if str(link.get('href')).find('{}page'.format(url)) != -1:
            result.update(compositions(str(link.get('href'))))
            continue
        result[str(link.string)] = str(link.get('href'))
    return result


def text(composition_link):
    response = requests.get(composition_link, timeout=1)
    soup = BeautifulSoup(response.text, 'lxml').find('div', id='entry_content')

    lines = ''
    for line in soup.contents:
        if any(str(line).find(bad_word) != -1 for bad_word in ['(', '[', '{']):
            continue

        if re.match(r'^<br.>', str(line)):
            lines += '\n'
            continue

        if re.match(r'^<a*', str(line)):
            line = line.text
        lines += str(line)

    result = ''
    for line in lines.split('\n'):
        if any(str(line).find(bad_word) != -1 for bad_word in ['Куплет:', 'Припев:', 'Премьера песни']):
            continue
        result += str(line) + '\n'

    return result


def all_texts(compositions_):
    for key in compositions_.keys():
        compositions_[key] = text(compositions_[key])
    return compositions_
