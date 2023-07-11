API_KEY = "2802b076d21c242db872ff1a9d720af7"
LAT = 40.7128
LON = 74.0060
EXCLUDE = "alerts"


'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'

import requests

# Replace 'YOUR_API_KEY' with your actual API key
weather_params = {
    "lat": 47.263489,
    "lon": -101.778008,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}
ONE_CALL_API = f"https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(ONE_CALL_API, params=weather_params)
response.raise_for_status()
weather_data = response.json()

hourly_weather = weather_data['hourly']



will_rain = False

for hour in hourly_weather[:12]:
    hour_weather_id = hour['weather'][0]['id']
    if hour_weather_id < 700:
        will_rain = True

if weather_data:
    print("Bring an umbrella")



# for hour in hourly_weather:
#     hour_dt = hour['dt']
#     hour_temp = hour['temp']
#     hour_feels_like = hour['feels_like']
#     hour_pressure = hour['pressure']
#     hour_humidity = hour['humidity']
#     hour_dew_point = hour['dew_point']
#     hour_uvi = hour['uvi']
#     hour_clouds = hour['clouds']
#     hour_visibility = hour['visibility']
#     hour_wind_speed = hour['wind_speed']
#     hour_wind_deg = hour['wind_deg']
#     hour_wind_gust = hour['wind_gust']
#     hour_weather = hour['weather'][0]
#     hour_weather_id = hour_weather['id']
#     hour_weather_main = hour_weather['main']
#     hour_weather_description = hour_weather['description']
#     hour_weather_icon = hour_weather['icon']
#
#     print(hour_temp)

    # Parsing the current weather data
    # current_weather = weather_data['current']
    # dt = current_weather['dt']
    # sunrise = current_weather['sunrise']
    # sunset = current_weather['sunset']
    # temp = current_weather['temp']
    # feels_like = current_weather['feels_like']
    # pressure = current_weather['pressure']
    # humidity = current_weather['humidity']
    # dew_point = current_weather['dew_point']
    # uvi = current_weather['uvi']
    # clouds = current_weather['clouds']
    # visibility = current_weather['visibility']
    # wind_speed = current_weather['wind_speed']
    # wind_deg = current_weather['wind_deg']
    # wind_gust = current_weather['wind_gust']
    # weather = current_weather['weather'][0]
    # weather_id = weather['id']
    # weather_main = weather['main']
    # weather_description = weather['description']
    # weather_icon = weather['icon']
    # print(weather_data)