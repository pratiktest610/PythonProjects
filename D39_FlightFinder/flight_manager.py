import requests
import datetime as dt

today = dt.datetime.now().date()
tomorrow = (today + dt.timedelta(days=1)).strftime(f"%d/%m/%Y")
next_date = (today + dt.timedelta(days=180)).strftime(f"%d/%m/%Y")


headers = {"apikey": "n9wQ-sw04vO6_7S2_5c3uk6OZSAi8pWp"}
IATA_endpoint = "https://tequila-api.kiwi.com/locations/query"


class FlightManager:

    def __init__(self):
        self.data = {}

    def iata_code(self, city):
        parameter = {"term": city}
        response = requests.get(url=IATA_endpoint, params=parameter, headers=headers)
        code = response.json()["locations"][0]["code"]
        return code

    def search(self, code):
        search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        parameters = {
            "fly_from": "NAG",
            "fly_to": code,
            "date_from": tomorrow,
            "date_to": next_date,
            "max_stopovers": 0,
            "curr": "INR",
            "limit": 1
        }

        response = requests.get(url=search_endpoint, params=parameters, headers=headers)
        self.data = response.json()

        try:
            data = self.data["data"][0]["route"][0]['local_departure'].split("T")[0]
        except IndexError:
            parameters["max_stopovers"] = 1
            response = requests.get(url=search_endpoint, params=parameters, headers=headers)
            self.data = response.json()
            return True
        else:
            return True




