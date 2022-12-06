import datetime as dt
import requests

today = dt.datetime.now().date()
from_date = today + dt.timedelta(days=1)
to_date = from_date + dt.timedelta(days =180)
print(from_date)

api_key = "n9wQ-sw04vO6_7S2_5c3uk6OZSAi8pWp"
location_search_endpoint = "https://tequila-api.kiwi.com/locations/query"
search_endpoint = "https://tequila-api.kiwi.com/search"
headers = {"apikey": api_key}


class FlightSearch:

    def __init__(self):
        self.cities = []
        self.codes = []
        self.data = []

    def get_codes(self,  city_list):
        """Returns a list of city code"""
        self.cities = city_list
        for city in self.cities:
            parameters = {"term": city}
            response = requests.get(url=location_search_endpoint, params=parameters, headers=headers)
            code = response.json()["locations"][0]["code"]
            self.codes.append(code)
        return self.codes

    def search_flight(self, codes):
        for code in codes:
            parameters = {
                "fly_from": "LCY",
                "fly_to": code,
                "date_from": from_date,
                "date_to": to_date,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
            }

            response = requests.get(url=search_endpoint, headers=headers, params=parameters)
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {code}.")
            else:
                price = data["price"]
                origin_city = data["route"][0]["cityFrom"]
                origin_airport = data["route"][0]["flyFrom"]
                destination_city = data["route"][0]["cityTo"]
                destination_airport = data["route"][0]["flyTo"]
                out_date = data["route"][0]["local_departure"].split("T")[0]
                return_date = data["route"][1]["local_departure"].split("T")[0]

                print(price)

