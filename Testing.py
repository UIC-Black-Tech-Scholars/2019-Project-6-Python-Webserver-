import requests

url = "http://localhost:8080"

data = {
    "python_key":"python_value"
}

r = requests.post(url=url, json=data)

print(r.status_code)
print(r.content)
print(r.text)