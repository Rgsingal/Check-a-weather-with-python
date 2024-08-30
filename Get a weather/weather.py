from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_kEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    
    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]}')
    print(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')
    return weather_data

if __name__ == "__main__":
  print('\n*** Get Current Weather Conditions ***\n')
  city = input("\nPlease enter a city name: ")
  weather_data = get_current_weather(city)
  print("\n")
  pprint(weather_data)
  #check for empty strings or strings with only spaces
  #if not bool(city.strip()): 
   #  city = "Sanjose"

   
  
