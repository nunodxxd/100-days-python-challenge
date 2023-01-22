import requests 
import os
from dotenv import load_dotenv

load_dotenv()

TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
API_KEY = os.getenv("API_KEY")

class FlightSearch:
     #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.api_key = API_KEY
        self.endpoint = TEQUILA_ENDPOINT
        self.headers = {
            "apikey": self.api_key,
        }

    def get_destination_code(self, city_name):
        location_endpoint = f"{self.endpoint}/locations/query"
        query = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=location_endpoint, headers=self.headers, params=query)
        results = response.json()["locations"]
        print(results[0]["code"])
        code = results[0]["code"]
        return code
    
    def get_destination_price(self, origin_city_code, destination_city_code, from_time, to_time):
        price_endpoint = f"{self.endpoint}/v2/search"
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR",
        }
        response = requests.get(url=price_endpoint, headers=self.headers, params=query)
        try:
            data = response.json()["data"][0]
            print(f"{data['cityTo']}: {data['price']}€")
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{self.endpoint}/v2/search",
                headers=self.headers,
                params=query,
            )
            try:
                data = response.json()["data"][0]
                print(f"{data['cityTo']}: {data['price']}€ via {data['route'][0]['cityTo']}")
                stepover=1
                via_city=data['route'][0]['cityTo']
                return (data,stepover,via_city)
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None
        return data