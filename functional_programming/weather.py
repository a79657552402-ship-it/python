import csv
import logging

import requests
import sys
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json

# Задание 3. Сделай CLI-утилиту weather.py, которая:
# принимает список городов (через аргументы CLI или файл),
# по каждому городу запрашивает координаты в геокодере Open-Meteo,
# по координатам получает почасовой прогноз на ближайшие 24 часа,
# считает t_min / t_max / t_avg и сохраняет результат в CSV.
# Требования:
#
# Использовать requests и requests.Session.
# Обязательно: таймауты, заголовок User-Agent, повторные попытки (Retry через HTTPAdapter).
# Аккуратно обрабатывать ошибки (сетевые, 4xx/5xx, «город не найден»).
# Кэшировать результаты геокодера на диск (простейший JSON-словарь city -> {lat, lon}{}), чтобы не дергать API повторно.
# Вывести прогресс в консоль (просто print или логирование).
# Выходной файл: forecast.csv со столбцами:city, date, t_min, t_max, t_avg


# 1. Нужно настроит CLI
# 2. Запрашиваем координаты в геокодере Open-Meteo через сайт https://geocoding-api.open-meteo.com/v1/search
# 3. По координатом получить погоду за последние 24 часа через сайт "https://api.open-meteo.com/v1/forecast"

logging.basicConfig(level=logging.INFO, stream=sys.stdout, filemode='w', encoding='utf-8',
                    format="[%(asctime)s] [%(levelname)s]:{%(message)s}")

retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=(429, 500, 502, 503, 504),
    allowed_methods=("GET",),
    raise_on_status=False,
)

adapter = HTTPAdapter(max_retries=retry)

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
CSV_PATH = "functional_programming/weather.csv"
CACHE_PATH = "functional_programming/geocode_cache.json"


def get_weather(cities):
    rows = []

    for city in cities:
        lat, lon, country = geocoder(city)
        weather = fetch_past_day_weather(lat, lon)
        hourly = weather.get("hourly")
        temps = hourly.get("temperature_2m")
        stats = calc_temp_stats(temps)
        if stats is None:
            logging.warning(f"[{city}] нет данных о температуре")
            continue
        t_min, t_max, t_avg = stats

        rows.append({
            "city": city,
            "country": country,
            "latitude": round(lat, 4),
            "longitude": round(lon, 4),
            "t_min": round(t_min, 1),
            "t_max": round(t_max, 1),
            "t_avg": round(t_avg, 1),
        })

    if rows:
        save_csv(rows)
    else:
        logging.warning("Нет данных для сохранения")


def geocoder(city):
    cache = load_cache()
    try:
        r = requests.get(
            GEOCODE_URL,
            params={"name": city, "count": 1, "language": "ru", "format": "json"},
            timeout=10,
            headers={"User-Agent": "weather-cli/1.0 (+https://example.com/weather-cli)"},
        )
        r.raise_for_status()  # возвращаем статус взоимодействия с сайтом
        data = r.json()
        logging.info(f"Данные полученые с джейсоном {data}")
    except requests.RequestException as e:
        logging.error(f"[{city}] ошибка сети: {e}")
        return None

    results = data.get("results")
    if not results:
        logging.warning(f"[{city}] город не найден")
        return None

    top = results[0]
    lat, lon = top["latitude"], top["longitude"]
    country = top.get("country", "")

    cache[city] = {"lat": lat, "lon": lon, "country": country}
    save_cache(cache)

    return lat, lon, country


def fetch_past_day_weather(lat, lon):
    try:
        r = requests.get(
            FORECAST_URL,
            params={
                "latitude": lat,
                "longitude": lon,
                "hourly": "temperature_2m",
                "past_days": 1,
                "forecast_days": 0,
                "timezone": "auto",
            },
            timeout=10,
            headers={"User-Agent": "weather-cli/1.0 (+https://example.com/weather-cli)"},
        )
        r.raise_for_status()
        data = r.json()
        temps = data.get("hourly", {}).get("temperature_2m", [])
        logging.info(f"temperature_2m ({len(temps)} значений): {temps}")
        return data
    except requests.RequestException as e:
        logging.warning(f"ошибка запроса погоды: {e}")
        return None


def calc_temp_stats(temps):
    valid = [t for t in temps]
    return min(valid), max(valid), sum(valid) / len(valid)


def save_csv(rows, path=CSV_PATH):
    fieldnames = ["city", "country", "latitude", "longitude", "t_min", "t_max", "t_avg"]
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    logging.info(f"Сохранено в {path} ({len(rows)} строк)")


def load_cache(path=CACHE_PATH):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        logging.warning(f"кэш повреждён, игнорирую: {e}")
        return {}


def save_cache(cache, path=CACHE_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    cities = sys.argv[1:]
    get_weather(cities)


if __name__ == "__main__":
    main()
