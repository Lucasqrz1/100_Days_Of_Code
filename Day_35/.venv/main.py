import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get ("OWN_API_KEY")
account_sid = "my_id"
auth_token = os.environ.get ("AUTH_TOKEN")




weather_params = {
    "lat": 42.679909,
    "lon": -70.837341,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWM_Endpoint, params=weather_params )
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = print(hour_data ["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            messaging_service_sid="my_id",
            body="Rain today! Bring an umbrella.",
            to="+myphone")
print(message.status)


