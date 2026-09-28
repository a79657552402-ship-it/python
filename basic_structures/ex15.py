# Дано целое число K.
# Вывести строку-описание оценки,
# соответствующей числу K(1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
# Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
import logging
import sys

logging.basicConfig(
    level=logging.WARNING,
    stream=sys.stdout
)


def inset_K():
    while True:
        print("введите оценку")
        K = int(input())
        if K < 1 or K > 5:
            logging.warning("Оценка не может быть меньше 1 и больше 5")
            print("введите ещё раз оценку")
            return inset_K()
        return K


def grade(K):
    match K:
        case 1:
            print("плохо")
        case 2:
            print("неудовлетворительно")
        case 3:
            print("удовлетворительно")
        case 4:
            print("хорошо")
        case 5:
            print("отлично")

K = inset_K()
grade(K)
