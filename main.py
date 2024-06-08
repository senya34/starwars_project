import requests

name = input('введите имя: ')
url = f'https://swapi.dev/api/people/?search={name}'


def find(url):
    response = requests.get(url=url)
    return response

result = find(url)
print(result.json())