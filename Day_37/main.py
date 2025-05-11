import requests

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = "https://pixe.la/v1/users/YOUR_USERNAME/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",

}


requests.post(url=graph_endpoint, json=graph_config)