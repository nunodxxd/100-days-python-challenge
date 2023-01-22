#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from typing import Tuple
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "LIS"
now = datetime.now()
six_month_from_today = now + timedelta(days=180)

def main():
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    sheet_data = data_manager.get_destination_data()

    need_iata = False
    for data in sheet_data:
        if data["iataCode"] == "":
            data["iataCode"] = flight_search.get_destination_code(data["city"])
            need_iata = True

    if need_iata:
        data_manager.update_destination_codes()

    #print(sheet_data)

    for data in sheet_data:
        data_flight = flight_search.get_destination_price(ORIGIN_CITY_IATA, data["iataCode"], now, six_month_from_today) 
        if data_flight != None:
            if data_flight == Tuple:
                flight_data = FlightData(data_flight[0],data_flight[1],data_flight[2])
            else:
                flight_data = FlightData(data_flight)
            data_manager.update_records(flight_data)
            if flight_data.price < data["lowestPrice"]:
                users = data_manager.get_customer_emails()
                emails = [row["email"] for row in users]
                notification_manager.send_email(flight_data,emails)   

main()