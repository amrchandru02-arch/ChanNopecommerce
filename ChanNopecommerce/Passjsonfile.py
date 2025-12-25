
import requests
import json

url = 'https://gorest.co.in/public/v2/users'

header = {
    'Content-Type' : 'application/json'
}
#req_payload = {
   # 'name': 'Jitendergggg Chopra',
   #'email': 'jitender_chopra@lubowitz-schumm.example'
#}
json_file = open('./users.json')
json_payload = json.load(json_file)
responce = requests.post(url, headers = header, json = json_payload)
print(responce.status_code)