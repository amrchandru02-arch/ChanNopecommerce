
import requests

url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities/12'

head = {
    'Accept' : 'text/plain',
    'Content-Type' : 'application/json'
}

req_payload = {
    
    "id": 77,
    "title": "chandru-Activity 12",
    "dueDate": "2025-12-24T21:51:24.1365169+00:00",
}

responce = requests.put(url, headers = head, json = req_payload)

print(responce.status_code)
assert responce.json()["title"] == "chandru-Activity 12"
print("assert is pass")