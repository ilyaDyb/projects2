from flask import current_app
import requests


"""4d243eb5-d00f-440b-ab27-d34f17590e94 """


def get_data():
    url = f'{current_app.config["WEATHER_URL"]}'
    headers = {'X-Yandex-API-Key': f'{current_app.config["API_KEY"]}'}
    params = {
        'lat': '55.755863',
        'lon': '37.6177',
        'lang': 'ru_RU',
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            result_json = response.json()
            return result_json
        else:
            return False

    except Exception as _ex:
        return False


def get_weather():
    result_json = get_data()

    try:
        forecasts = result_json['forecasts'][0]
        weather_day = forecasts['parts']['day']
        date = forecasts['date']
        sunrise = forecasts["sunrise"]
        sunset = forecasts["sunset"]
        temp_min = weather_day["temp_min"]
        temp_avg = weather_day["temp_avg"]
        wind_speed = weather_day["wind_speed"]
        wind_dir = weather_day["wind_dir"]
        pressure_mm = weather_day["pressure_mm"]

    except Exception as _ex:
        return False

    all_info = f"Дата: {date}\nВосход: {sunrise}\nЗакат: {sunset}\nМин. Температура: {temp_min}\nСред. Температура: {temp_avg}\nСкорость ветра: {wind_speed}м/с\nНаправление ветра: {wind_dir}\nДавление: {pressure_mm}мм рт.ст"
    return all_info.split('\n')


if __name__ == "__main__":
    print(get_weather())