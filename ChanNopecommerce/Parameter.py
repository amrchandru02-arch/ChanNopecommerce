
import requests

url = 'https://gorest.co.in/public/v2/users'

paramet = {
    'page' : 2,
    'per_page' : 4
}
responce = requests.get(url, params = paramet)
print(responce.json())
print(responce.status_code)
assert responce.status_code == 200
