# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from .base_query import BaseQuery


class TextLyricsQuery(BaseQuery):
    def __init__(self):
        super().__init__()
        self._site = 'text-lyrics.ru'
        self._alphabet = dict(zip('abcdefghijklmnopqrstuvwxyz1234567890абвгдеёжзиклмнопрстуфхцчшщэюя', list('abcdefghijklmnopqrstuvwxyz1234567890') + 'a1 b1 v1 g1 d1 e1 e1 gg z1 i1 k1 l1 m1 n1 o1 p1 r1 c1 t1 u1 f1 x1 z2 ch sh sh1 e2 yu i2'.split(' ')))

    def artists(self, first_symbol: str) -> {str: str}:
        first_symbol = self._alphabet.get(first_symbol.lower())
        url = 'https://{}/{}.html'.format(self._site, first_symbol)
        response = requests.get(url, timeout=self._timeout)

        href = re.compile('^http://{}/{}/*'.format(self._site, first_symbol))
        soup = BeautifulSoup(response.text, 'lxml').findAll('a', href=href)
        return {str(link.string): str(link.get('href')) for link in soup}

    def compositions(self, artist: str, find_pages: bool = True) -> {str: str}:
        url = artist if artist.find(self._site) != -1 else self.artists(str(artist[0])).get(artist)
        response = requests.get(url, timeout=self._timeout)
        url = url.replace('http://', 'https://')

        result = {}
        for link in BeautifulSoup(response.text, 'lxml').findAll('a', href=re.compile('^{}*'.format(url))):
            if not (link.get('class') is None):
                continue

            if str(link.get('href')).find('{}page'.format(url)) != -1:
                if find_pages:
                    for key, value in self.compositions(str(link.get('href')), find_pages=False).items():
                        if value not in result.values():
                            result[key] = value
                continue

            key = str(link.string)
            value = str(link.get('href'))
            if key not in ['\n', '', None] and value not in result.values():
                result[key] = value

        return result

    def text(self, composition_link: str) -> {str: [str]}:
        response = requests.get(composition_link, timeout=self._timeout)
        soup = BeautifulSoup(response.text, 'lxml')

        if soup.find('a', href='https://text-lyrics.ru/translate/'):
            return None

        def parse_lines(lines):
            res = u''
            for line in lines:
                if re.match(r'<p>', str(line)):
                    res += parse_lines(line)
                    continue

                if re.match(r'<br.>', str(line)):
                    res += '\n'
                    continue

                if re.match(r'<a*', str(line)):
                    line = line.text

                res += str(line)
            return res

        text = parse_lines(soup.find('div', id='entry_content').contents)
        return text
