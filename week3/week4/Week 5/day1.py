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
#API - to fetch temperature of a city
city_name = input("Enter city name: ")
api_key = '409bf2685494c84529105b1a367e42ec'

#Building API URL
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_response = requests.get(api_url)
data= get_server_response.json()
print(f"City: {data['name']}, Temperature: {data['main']['temp']}°C, Weather: {data['weather'][0]['description']}")
