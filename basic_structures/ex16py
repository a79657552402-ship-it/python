# Даны два целых числа: D(день) и M (месяц),
# определяющие правильную дату невисокосного года. Вывести значения D и M для даты, следующей за указанной.
import logging
import sys

logging.basicConfig(
    level=logging.WARNING,
    stream=sys.stdout
)


def insert_day_and_month():
    print("Введите день:")
    D = int(input())
    print("введите месяц:")
    M = int(input())

    if D < 1 or D > 31 or M < 1 or M > 12:
        logging.warning("Введины не валидные данные, повторите попытку:")
        return insert_day_and_month()
    return D, M


#         4 6 9 11
def next_day(D, M):
    while True:
        match M:
            case 1 | 3 | 5 | 7 | 8 | 10:
                if D > 31:
                    logging.warning(f"в {M} месяце количество дней не может превышать 31 дня")
                if D == 31:
                    print(f"1/{M + 1}")
                else:
                    print(f"{D + 1}/{M}")
                return
            case 12:
                if D > 31:
                    logging.warning(f"в {M} месяце количество дней не может превышать 31 дня")
                if D == 31:
                    print(f"1/1")
                else:
                    print(f"{D + 1}/{M}")
                return
            case 4 | 6 | 9 | 11:
                if D > 30:
                    logging.warning(f"в {M} месяце количество дней не может превышать 30 дня")
                if D == 30:
                    print(f"01/{M + 1}")
                else:
                    print(f"{D + 1}/{M}")
                return
            case 2:
                if D > 28:
                    logging.warning(f"во {M} месяце количество дней не может превышать 28 дня, повторите попытку:")
                    D, M = insert_day_and_month()
                    continue
                if D == 28:
                    print(f"1/{M + 1}")
                else:
                    print(f"{D + 1}/{M}")
                return


D, M = insert_day_and_month()
next_day(D, M)
