import time
from concurrent.futures import ThreadPoolExecutor

import requests

# 3. Реализуйте асинхронный код, который отправляет 50 запросов по адресу http://google.com/ или https://example.com/.
#  Ограничьте одновременное количество возможных запросов до 10.
# Статус-коды ответов запишите в файл. Количество запросов requests_amount,
#  лимит одновременно выполняемых запросов requests_limit и url должны передаваться как входные аргументы функции.

def get_url(url: str, requests_amount: int, requests_limit: int):
    start = time.perf_counter()

    def fetch(i: int):
        try:
            response = requests.get(url)
            return i, response.status_code
        except requests.RequestException as e:
            return i, f"ERROR: {type(e).__name__}"

    with ThreadPoolExecutor(max_workers=requests_limit) as executor:
        results = list(executor.map(fetch, range(requests_amount)))

    end = time.perf_counter()
    ok = sum(1 for i, s in results if s == 200)

    with open('statuses.txt', "w", encoding="utf-8") as f:
        for i, status in results:
            f.write(f"Запрос {i + 1}: {status}\n")
        f.write("\n")
        f.write(f"{requests_amount} запросов c масксимально одновременно выполненых запросов (лимит {requests_limit}) выполняется за {end -start:.2f} сек\n")
        f.write(f"Успешных (200): {ok}/{requests_amount}\n")
    print(f"Статусы записаны в 'statuses.txt'")

    return results


if __name__ == "__main__":
    get_url("https://www.google.com/", requests_amount=50, requests_limit=10)
