
import requests
Head = {
    'Accept':'text/plain'
}
responce = requests.get("https://jsonplaceholder.typicode.com/posts/1", headers = Head)

print(responce.status_code)
print(responce.json())
assert responce.status_code == 200