import requests
from datetime import datetime

USERNAME = "adrian15"
TOKEN = "seri9832nmKAW"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# TODO #1: Create user account
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)  # prints response message

# TODO #2: Create a graph definition
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "min",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Graph already created
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# TODO #3: Get the graph
# View graph: https://pixe.la/v1/users/adrian15/graphs/graph1.html

# Create pixel
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# TODO #4: Post value to the graph
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
