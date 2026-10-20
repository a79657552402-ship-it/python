# Задание 4: Продвинутые comprehensions
# Создайте систему анализа текста, используя различные comprehensions:
# Словарь частотности слов из списка текстов
# Вложенный словарь статистики по каждому тексту
# Множество уникальных слов длиннее N символов
# Генератор для обработки текста по частям
#
# Требования:
# Используйте dict, set, list comprehensions и generator expressions
# Реализуйте вложенные comprehensions
# Обработайте edge cases (пустые строки, специальные символы)
# Требования:
# Используйте functools, itertools
# Реализуйте универсальные функции, работающие с любыми данными
# Добавьте обработку ошибок

import re
from collections import Counter

# Словарь частотности слов из списка текстов
"""Имеется введу что ключом будет слово, а его значение это количество повторов этого слова"""
def dct_repeat(text):
    if not isinstance(text, str):
        raise TypeError('Текст должен быть стракой!!!')
    if not text:
        raise ValueError('Текст не может быть пустым!!!')
    words = re.findall(r'\w+', text.lower())
    dct = {k: words.count(k) for k in words}
    print(dct)
# with open('poem.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
# dct_repeat(text)
# dct_repeat(123)
# text= ''
# dct_repeat(text)

# Вложенный словарь статистики по каждому тексту
def nested(*texts):
    if not texts:
        raise ValueError('Нужен хотя бы один текст')
    for text in texts:
        if not isinstance(text, str):
            raise TypeError('Аргумент должен быть строкой')
        if not text:
            raise ValueError('Текст не может быть пустым')
    return {
        f'text{i}': dict(Counter(re.findall(r'\w+', text.lower())))
        for i, text in enumerate(texts)
    }
# with open('poem.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
# with open('poem_2.txt', 'r', encoding='utf-8') as file:
#     text_2 = file.read()
# print(nested(text, text_2))
# print(nested())
# print(nested(123, 345))
# text = ''
# print(nested(text))

# Множество уникальных слов длиннее N символов
def set_len(text, N):
    if not isinstance(text, str):
        raise TypeError('Текст должен быть стракой!!!')
    if not text:
        raise ValueError('Текст не может быть пустым!!!')
    if N < 0 or N>len(text):
        raise ValueError('Длина символов не может быть меньше нуля или больше длины текста')
    words = re.findall(r'\w+', text.lower())
    st = {k for k in words if len(k) > N}
    return (st)
# with open('poem.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
# print(set_len(text, 4))
# print(set_len('fdgdgd', -1))
# print(set_len('fdgdgd', 20))

# Генератор для обработки текста по частям
def text_chunks(text, chunk_size):
    if not isinstance(text, str):
        raise TypeError('Текст должен быть строкой!!!')
    if not text:
        raise ValueError('Текст не может быть пустым!!!')
    if not isinstance(chunk_size, int):
        raise TypeError('chunk_size должен быть целым числом!!!')
    if chunk_size <= 0:
        raise ValueError('chunk_size должен быть больше нуля!!!')
    tokens = re.findall(r'\S+', text)
    buffer = []
    current_len = 0

    for token in tokens:
        token_len = len(token) + (1 if buffer else 0)
        if buffer and current_len + token_len > chunk_size:
            yield ' '.join(buffer)
            buffer = [token]
            current_len = len(token)
        else:
            buffer.append(token)
            current_len += token_len
    if buffer:
        yield ' '.join(buffer)

with open('poem.txt', 'r', encoding='utf-8') as file:
    text = file.read()

for chunk in text_chunks(text, 50):
    print(chunk)

parts_info = (
    {'часть': i, 'кол-во символов': len(chunk), 'кол-во слов': len(re.findall(r'\w+', chunk))}
    for i, chunk in enumerate(text_chunks(text, 50), 1))
for info in parts_info:
    print(info)