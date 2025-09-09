import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print(f'Статус код :{result.status_code}')
assert 200 == result.status_code
if result.status_code == 200:
    print("Успех. Мы получили новую шутку")
else:
    print("Провал")
result.encoding = 'utf-8'
print(result.text)