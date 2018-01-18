import sys
import requests

url = sys.argv[1]
response = requests.get(url)
print(response.status_code)
with open("test_week5.py", 'wb') as png:
    png.write(response.content)
print("Everything OK ")
