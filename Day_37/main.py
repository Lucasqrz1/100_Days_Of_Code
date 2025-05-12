import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74"
}

try:
    response = requests.post(
        url=pixel_creation_endpoint, 
        json=pixel_data, 
        headers=headers
    )
    response.raise_for_status()  # Raises an HTTPError for bad responses
    print(f"Success! Status code: {response.status_code}")
    print(f"Response: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")