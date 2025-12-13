import requests
import json

request = requests.get(url="https://www.flipkart.com/")
assert request.status_code==201, f"Validation failed"
print(request.status_code)


