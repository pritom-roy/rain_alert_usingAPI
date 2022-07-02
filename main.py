import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("api")

account_sid = os.environ.get("sid")
auth_token = os.environ.get("token")

parameter = {
    "lat": 24.894930,
    "lon": 91.868706,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)
data.raise_for_status()
data = data.json()

temp = 0

for x in range(12):
    if data["hourly"][x]["weather"][0]["id"] < 700:
        temp = 1
        break

if temp == 1:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bring an Umbrella ☂",
        from_="+18508018265",
        to="+8801732792640"
    )

    print(message.status)
