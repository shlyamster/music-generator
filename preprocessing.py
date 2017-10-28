# -*- coding: utf-8 -*-
import re
import json
from collections import Counter


def read_text(file_name: str) -> {}:
    with open(file_name, 'r') as json_file:
        return json.loads(json_file.read())


def remove_keywords(text: str, keywords: [str] = None) -> str:
    if keywords is None:
        keywords = [
            'Куплет:', 'Припев:', 'Припев :', 'Аутро:', 'Интро:',
            'Интро:', 'Verse 1:',
            'Премьера песни', 'Премьера песни ', 'Премьера песни "',
            '" состоялась -', 'Перед припевом:',
            'Вступление:', 'Бридж:',
            'Переход:',
            'Куплет 1:', 'Куплет 2:', 'Куплет 3:'
        ]

    def no_any_keyword(line):
        def find_keyword(keyword):
            return line.find(keyword) != -1
        return not any(map(find_keyword, keywords))

    return '\n'.join(filter(no_any_keyword, text.split('\n')))


def remove_bad_chars(text: str) -> str:
    text = re.sub(r'[\{\(\[].*[\{\)\]]', '', text)

    text = re.sub(r'(?!\s)\W ', ' ', text)
    text = re.sub(r'(?!\s)\W(?!\n)', ' ', text)
    text = re.sub(r'(?!\s)\W\n', '\n', text)

    text = re.sub(r'(?!\n)\s{2,}', ' ', text)
    text = re.sub(r'\n\s+', '\n', text)
    text = re.sub(r'\n{2,}', '\n', text)
    return text


def process(text: str) -> str:
    text = remove_keywords(text)
    text = remove_bad_chars(text)
    text = text.lower()
    return text


def unique_lines(text: str) -> Counter:
    return Counter(text.split('\n'))


if __name__ == '__main__':
    text = read_text('data/raw/super_texts.json')

    total_text = u''
    for key, value in sorted(text.items()):
        total_text += str(value) + '\n'

    total_text = process(total_text)
    print(total_text)
    exit()
    lines = unique_lines(total_text)
    print('\n'.join(map(str, lines.most_common(50))))
