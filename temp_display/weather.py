import requests

def weather(place):
    apikey =open("temp_display\keys","r").read()

    city = place

    loc_url = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&limit=5&appid=" + apikey

    response_loc = requests.get(loc_url).json()
    latitute = response_loc[0]["lat"]
    longitude = response_loc[0]["lon"]

    weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitute) + "&lon=" + str(longitude) + "&appid=" + apikey

    response_weather = requests.get(weather_url).json()

    print(round(response_weather["main"]["temp"] - 273.15,2), round(response_weather["main"]["feels_like"] - 273.15, 2))

    temp = round(response_weather["main"]["temp"] - 273.15,2)
    feels_like = round(response_weather["main"]["feels_like"] - 273.15, 2)

    return temp, feels_like