#API
# In VS Code (requires: pip install requests)
#import requests

#url = 'https://randomfox.ca/floof'


#response = requests.get(url)
#rint(response.headers)
#print(response.text)
#print(response.json())
#print(response.json()["image"])
#data=response.json()
#print(f"Fox image: {data['image']}")
#print(data['link'])

import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .env is in the same folder as this script, so no path needed

city_name = input("Enter city name: ")
api_key = os.environ.get("OPENWEATHER_API_KEY")

api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_response = requests.get(api_url)
data = get_server_response.json()

if data.get("cod") != 200:
    print(f"Error: {data.get('message', 'City not found')}")
else:
    print(f"City: {data['name']}, Temperature: {data['main']['temp']}°C, Weather: {data['weather'][0]['description']}")
