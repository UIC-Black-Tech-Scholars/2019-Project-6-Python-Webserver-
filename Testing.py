import requests

url = "http://localhost:8080"

data = {
    "Key":"Value"
}

r = requests.post(url=url, data=data)

print(r.status_code)
print(r.content)
print(r.text)