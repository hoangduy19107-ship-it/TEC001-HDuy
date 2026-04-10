import os
import requests

API_KEY = "d518861ecf5fe849b109f7a7adb8c654"

municipality = input("Enter municipality: ")

if not API_KEY:
    print("Error: set the OPENWEATHER_API_KEY environment variable with your OpenWeather API key.")
else:
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={API_KEY}"

    response = requests.get(api_url)

    if response.status_code != 200:
        try:
            error_data = response.json()
            message = error_data.get('message', 'Unknown error')
        except ValueError:
            message = response.text
        print(f"Error fetching weather: {message}")
    else:
        data = response.json()
        weather = data.get('weather', [])
        main = data.get('main', {})

        if not weather or 'temp' not in main:
            print("Weather information not available.")
        else:
            description = weather[0].get('description', 'No description')
            temp_kelvin = main['temp']
            temp_celsius = temp_kelvin - 273.15
            print(f"Weather: {description}")
            print(f"Temperature: {temp_celsius:.2f} °C")
