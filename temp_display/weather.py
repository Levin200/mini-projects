import requests

def weather(place):
    # read the secret API keys
    apikey =open("temp_display\keys","r").read()

    city = place

    #get the location use Geocoding API to get latitude and logitude
    loc_url = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&limit=5&appid=" + apikey

    response_loc = requests.get(loc_url).json()
    latitute = response_loc[0]["lat"]
    longitude = response_loc[0]["lon"]

    # get the wheater information
    weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitute) + "&lon=" + str(longitude) + "&appid=" + apikey

    response_weather = requests.get(weather_url).json()

    #print(round(response_weather["main"]["temp"] - 273.15,2), round(response_weather["main"]["feels_like"] - 273.15, 2))
    # convert the temperature from kelvin to degree celcius

    temp = round(response_weather["main"]["temp"] - 273.15,2) 
    feels_like = round(response_weather["main"]["feels_like"] - 273.15, 2)

    # get description of the weather if it sunny, rainy,etc 
    description = response_weather["weather"][0]["description"]
    # get the image icon code
    icon = response_weather["weather"][0]["icon"]

    return temp, feels_like, description, icon