import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

def get_env_variable(var_name):
    value = os.environ.get(var_name)
    if not value:
        raise ValueError(f"Environment variable {var_name} is not set")
    return value

def check_weather(api_key, lat, lon):
    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "cnt": 4,
    }
    
    try:
        response = requests.get(OWM_Endpoint, params=weather_params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def will_rain_today(weather_data):
    if not weather_data:
        return False
        
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            return True
    return False

def send_sms_alert(account_sid, auth_token, msg_service_sid, to_number):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            messaging_service_sid=msg_service_sid,
            body="Rain today! Bring an umbrella.",
            to=to_number
        )
        return message.status
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return None

def main():
    try:
        # Get environment variables
        api_key = get_env_variable("OWN_API_KEY")
        account_sid = get_env_variable("TWILIO_ACCOUNT_SID")
        auth_token = get_env_variable("AUTH_TOKEN")
        msg_service_sid = get_env_variable("TWILIO_MSG_SERVICE_SID")
        to_number = get_env_variable("TO_PHONE_NUMBER")
        
        # Configuration
        OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
        LAT = 42.679909
        LON = -70.837341

        # Check weather
        weather_data = check_weather(api_key, LAT, LON)
        
        # Send alert if needed
        if will_rain_today(weather_data):
            status = send_sms_alert(account_sid, auth_token, msg_service_sid, to_number)
            print(f"Message status: {status}")
        else:
            print("No rain expected today")

    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()