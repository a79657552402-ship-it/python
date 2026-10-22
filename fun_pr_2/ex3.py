import os
# Задание 3: Продвинутые comprehensions
# Создайте систему анализа текста, используя различные comprehensions:
#
# Словарь частотности слов из списка текстов
# Вложенный словарь статистики по каждому тексту
# Множество уникальных слов длиннее N символов
# Генератор для обработки текста по частям
# Требования:
#
# Используйте dict, set, list comprehensions и generator expressions
# Реализуйте вложенные comprehensions
# Обработайте edge cases (пустые строки, специальные символы)
# Требования:
#
# Используйте functools, itertools
# Реализуйте универсальные функции, работающие с любыми данными
# Добавьте обработку ошибок


import string
from collections import Counter
from functools import partial

"""Чтение и изьятие текста из файла, получаем входные данные в виде списка без пробелов и перносов"""
def insert_data(file):
    with open(file, 'r', encoding='utf8') as text:
        content = text.read()
    words = []
    for line in content.splitlines():
        for word in line.split():
            clean = word.strip(string.punctuation)
            if clean:
                words.append(clean.lower())
    return words


"""Словарь частотности слов из списка текстов"""
def word_frequency(text):
    return dict(Counter(text).most_common())

"""Вложенный словарь статистики по каждому тексту, подсчитаем сколько всего слов"""
def statisitc_word(N, dct):
    dct_statisitc_word = {
        'Количество слов': sum(dct.values()),
        'Количество слов содержащих букв больше чем переданное значение': len(set_words(N, dct)),
        'Самое короткое слово:': min(dct, key=len),
        'Самое длиное слово:': max(dct, key=len)
    }
    return dct_statisitc_word

"""Множество уникальных слов длиннее N символов"""
def set_words(N, dct):
    words = {word for word in dct if len(word) > N}
    return words

"""Генератор для обработки текста по частям"""
def insert_data_gen(file):
    with open(file, 'r', encoding='utf8') as text:
        for line in text:
            clean = line.strip()
            if clean:
                yield clean

"""Промежуточный генератор: строки → слова."""
def split_words(lines_iter):
    for line in lines_iter:
        for word in line.split():
            clean = word.strip(string.punctuation)
            if clean:
                yield clean.lower()

"""Обёртка над insert_data: файл не существует / пустой / битая кодировка."""
def safe_insert_data(file):
    if not os.path.exists(file):
        print(f"[!] Файл не найден: {file}")
        return []
    try:
        return insert_data(file)
    except (UnicodeDecodeError, OSError) as e:
        print(f"[!] Ошибка чтения {file}: {e}")
        return []

"""Обёртка над word_frequency: пустой вход → {}."""
def safe_word_frequency(text_iter):
    try:
        return word_frequency(text_iter)
    except (AttributeError, TypeError):
        # на случай, если пришёл исчерпанный/неправильный объект
        return {}

"""Обёртка над statisitc_word: пустой словарь → нулевая статистика."""
def safe_statisitc_word(N, dct):
    if not dct:
        return {
            'Количество слов': 0,
            'Количество слов содержащих букв больше чем переданное значение': 0,
            'Самое короткое слово:': None,
            'Самое длиное слово:': None,
        }
    return statisitc_word(N, dct)

"""Обёртка над set_words: пустой словарь → пустое множество."""
def safe_set_words(N, dct):
    if not dct:
        return set()
    return set_words(N, dct)

"""Обёртка над insert_data_gen: файл не существует → пустой генератор."""
def safe_insert_data_gen(file):
    if not os.path.exists(file):
        print(f"[!] Файл не найден: {file}")
        return
    try:
        yield from insert_data_gen(file)
    except (UnicodeDecodeError, OSError) as e:
        print(f"[!] Ошибка чтения {file}: {e}")

"""Обёртка над split_words: страхует от «мусорных» токенов."""
def safe_split_words(lines_iter):
    for line in lines_iter:
        for word in line.split():
            clean = word.strip(string.punctuation)
            if clean:
                yield clean.lower()


print('========== Результат полученый через функцию===========')
statisitc_word_part = partial(statisitc_word, 5)
print(statisitc_word_part(word_frequency(insert_data('poem.txt'))))

print('========== Результат полученый через генератор===========')
print(set_words(5, word_frequency(split_words(insert_data_gen('poem.txt')))))
print(statisitc_word_part(word_frequency(split_words(insert_data_gen('poem.txt')))))

print('нормальный файл')
print(safe_statisitc_word(5, safe_word_frequency(safe_insert_data('poem.txt'))))

print('несуществующий файл')
print(safe_statisitc_word(5, safe_word_frequency(safe_insert_data('nofile.txt'))))

print('пустой файл')
print(safe_statisitc_word(5, safe_word_frequency(safe_insert_data('empty.txt'))))

print('файл только из пунктуации/пробелов')
print(safe_statisitc_word(5, safe_word_frequency(safe_insert_data('blank.txt'))))

print('через генератор + обёртки')
print(safe_statisitc_word(5, safe_word_frequency(safe_split_words(safe_insert_data_gen('poem.txt')))))

print('пустой генератор')
print(safe_statisitc_word(5, safe_word_frequency(safe_split_words(safe_insert_data_gen('empty.txt')))))