import requests
url="https://www.ceneo.pl/45534929#tab=reviews"
response= requests.get(url)
print(response.text)