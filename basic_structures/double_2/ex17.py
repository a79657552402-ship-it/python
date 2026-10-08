import logging
import sys

# Откройте и прочитайте данные с файла txt, способом, который рассматривается в видео из пункта 1.

logging.basicConfig(level=logging.INFO, stream=sys.stdout, filemode='w', encoding='utf-8',
                    format="[%(asctime)s] [%(levelname)s]:{%(message)s}")

file = open('hello.txt','a', encoding='utf-8')

file.write('HELLOW !!!!\n')
file.write('HELLOW !!!!\n')
file.write('HELLOW !!!!')
# print(file)


# s = file.readlines()
# print(s)
# for row in file:
#     for letter in row:
#         print(letter)

# print(file.read(3))

# logging.info(f'Содержимая файла:\n {f}')