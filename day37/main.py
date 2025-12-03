import requests
from datetime import datetime

TOKEN = "jfsdgfjshghuhowhj"
USERNAME = "asfandiyor1"
pixels_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph2"

users_parems= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixels_endpoint, json=users_parems)
#  print(response.text)

endpoint_graph = f"{pixels_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id" : GRAPH_ID,
    "name" : "Coding day",
    "unit" : "hour",
    "type": "float",
    "color": "ajisai"

}
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create graph

# response = requests.post(url=endpoint_graph, json=graph_config, headers=headers)
# print(response.text)
# Create pixel

pixel_creation_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
#today = datetime.now(#year = 2020, month = 2 , day = 5)
print(today)

pixel_date = {
    "date" : today.strftime("%Y%m%d"),
    "quantity":input("how many times - "),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_date, headers=headers)
print(response.text)

# delete_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)