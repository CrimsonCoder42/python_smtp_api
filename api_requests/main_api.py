import requests
from datetime import datetime

MY_LAT = 40.7128
MY_LNG = -74.0060


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
print(longitude)
print(latitude)

iss_position = (longitude, latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

def split_and_clean(time_data):
    if "T" in time_data:
        new_data = time_data.split("T")[1].split(":")
        return new_data
    else:
        new_data = time_data.strftime("%H:%M:%S.%f")[:-3]
        return new_data

def night_time(rise, set, now):
    return rise > now or set < now


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
time_now = datetime.now()
time_str = time_now.strftime("%H:%M:%S.%f")[:-3]

sunrise_hour = split_and_clean(sunrise)[0]
sunset_hour = split_and_clean(sunset)[0]
time_now_hour = time_str[0:2]


print(night_time(sunrise_hour, sunset_hour, time_now_hour))




