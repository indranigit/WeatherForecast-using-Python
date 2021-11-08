pip install requests

import requests

city=input("Enter your city name")

print(city)

print("Displaying Weather Report for: " + city)

url='https://wttr.in/{}'.format(city)

result=requests.get(url)

print(result.text)

