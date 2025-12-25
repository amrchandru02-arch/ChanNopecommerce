import requests

# 1️⃣ LOGIN API – Get Token
login_url = "https://reqres.in/api/login"

login_payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

login_response = requests.post(login_url, json=login_payload)

print("Login Status:", login_response.status_code)
print("Login Response:", login_response.json())

# 2️⃣ Extract token
token = login_response.json().get("token")

if not token:
    raise Exception("Token not received from login API")

print("Token:", token)

# 3️⃣ Authorized POST request
url = "https://reqres.in/api/users"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

payload = {
    "name": "Sneha",
    "job": "QA Engineer"
}

response = requests.post(url, json=payload, headers=headers)

print("Create User Status:", response.status_code)
print("Create User Response:", response.json())
