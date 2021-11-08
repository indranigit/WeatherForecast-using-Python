#import the neccessary package
import requests

#Take city name as user  input
city=input("Enter your city name")

print(city)

print("Displaying Weather Report for: " + city)

#Fetch the weather deatils from wttr.in
url='https://wttr.in/{}'.format(city)

#Store the result in result variable
result=requests.get(url)

#display the result
print(result.text)

