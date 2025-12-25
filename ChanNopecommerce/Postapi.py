
import requests

url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'
head = {
    'accept' : 'text/plain',
    'Content-Type' : 'application/json'
}
payload =  {
  "id": 99,
  "title": "chandru-amareshwar",
  "dueDate": "2025-12-24T07:16:05.051Z",
  
}
responce = requests.post(url, headers =head, json = payload)

assert responce.status_code == 200
assert responce.json()["title"] == 'chandru-amareshwar'
print("assert is pass")
