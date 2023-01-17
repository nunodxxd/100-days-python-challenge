import requests
from twilio.rest import Client

end_point = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your_api_key"
city = "lisbon"
MY_LAT = 38.736946
MY_LONG = -9.142685

account_sid = "your_account_sid"
auth_token = "your_auth_token"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=end_point, params=parameters)
response.raise_for_status()
data = response.json()

#first 12 hours of the data
weather_slice = data["hourly"][:12]

will_rain = False
#check if any of the next 12 hours have rain in them and if so, send a text message
for hour_data in weather_slice:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_='your_twilio_number',
            to='your_phone_number'
        )

    print(message.status)