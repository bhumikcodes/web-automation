import requests
import json

request = requests.get(url="https://www.flipkart.com/")
assert request.status_code==200
print(request.status_code)
print(request.text)

print("ok")


