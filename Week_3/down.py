import sys
import requests

url = sys.argv[1]
response = requests.get(url)
with open("picture.png", 'wb') as png:
    png.write(response.content)
print("Everything OK ")
