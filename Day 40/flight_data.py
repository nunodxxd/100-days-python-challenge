class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data,stop_overs=0,via_city=""):
        self.price = data["price"]
        self.origin_city = data["cityFrom"]
        self.origin_airport = data["flyFrom"]
        self.destination_city = data["cityTo"]
        self.destination_airport = data["flyTo"]
        self.out_date = data["route"][0]["local_departure"].split("T")[0]
        self.return_date = data["route"][1]["local_departure"].split("T")[0]
        self.stop_overs = stop_overs
        self.via_city = via_city
    