import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv('SHEETY_PRICES_ENDPOINT')
SHEETY_USERS_ENDPOINT = os.getenv('SHEETY_USERS_ENDPOINT')
SHEETY_PRICES_RECORD_ENDPOINT = os.getenv('SHEETY_PRICES_RECORD_ENDPOINT')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.header = {"Authorization" : f"{SHEETY_TOKEN}"}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.header)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            #print(response.text)

    def update_records(self,flight_data):
        for city in self.destination_data:
            if city["city"] == flight_data.destination_city:
                new_record = {
                    "pricerecord": {
                        "lowestPriceEver": flight_data.price,
                        "date": f"{flight_data.out_date} - {flight_data.return_date}"
                    }
                }
                response = requests.put(
                    url=f"{SHEETY_PRICES_RECORD_ENDPOINT}/{city['id']}",
                    json=new_record
                )
                #print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.header)
        response.raise_for_status()
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data