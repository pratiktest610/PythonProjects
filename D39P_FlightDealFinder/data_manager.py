# This class is responsible for talking to the Google Sheet.

import requests
get_endpoint = "https://api.sheety.co/c3fcb965379cf87aa728fed166797a3b/flightDeals/prices"
headers = {"Authorization": "Bearer herejryjytkreeyw3y468o68lew4y"}

# response = requests.get(url=get_endpoint)
# rows = response.json()["prices"]
# print(rows)
# codes = []
# for row in rows:
#     code = row["iataCode"]
#     codes.append(code)
# print(codes)



class DataManager:
    def __init__(self):
        response = requests.get(url=get_endpoint, headers=headers)
        self.sheet = response.json()
        self.rows = self.sheet["prices"]
        self.cities = []
        self.codes = []
        self.id = 1

    def get_cities(self):
        """Returns list of cities from sheet """
        for row in self.rows:
            city = row["city"]
            self.cities.append(city)
        return self.cities

    def get_codes(self):
        for row in self.rows:
            code = row["iataCode"]
            self.codes.append(code)
        return self.codes



    def load_codes(self, code_list: list):
        """ loads up iata codes in sheets"""
        for i in range(len(code_list)):
            self.rows[i]["iataCode"] = code_list[i]

        for row in self.rows:
            parameters = {
                "price": row
            }
            self.id += 1
            put_endpoint = f"https://api.sheety.co/c3fcb965379cf87aa728fed166797a3b/flightDeals/prices/{self.id}"
            response = requests.put(url=put_endpoint, json=parameters, headers=headers)





