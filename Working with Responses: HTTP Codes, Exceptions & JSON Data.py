import requests

response = requests.get(url="http//api.open_notyfy.org/iss-now.json")
print(response.status_code)
