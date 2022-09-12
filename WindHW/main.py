import requests

response = requests.get('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0')
data = response.json()
point_number = 11
wind = data['dataseries'][point_number]['wind10m']
print(wind)