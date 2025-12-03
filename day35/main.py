import os

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpont = "https//api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_APO_KEY")
account_sid = "AC7c357bb2c70d78979800"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 51.587351,
    "lon": -0.127758,
    "appid": api_key,
    "cnt" : 4
}

response = requests.get(OWM_Endpont, params= weather_params)
response.raise_for_status()
weather_date = response.json()
#print(weather_date[list])


will_rain = False
for hour_date in weather_date["list"]:
    condition_code = hour_date["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = "Join Earth mightiest heroes. Like Kevin Bacon",
        from = "+15017122661",
        to="YOu verified number "
    )
    print(message.status)