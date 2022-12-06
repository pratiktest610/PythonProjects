import requests

sheet_headers = {"Authorization": "Bearer rg3f22ff3w4f3f4f"}


class SheetManager:

    def __init__(self):
        sheet_endpoint = "https://api.sheety.co/b3a71263788566b08e78e5d530defc94/flightDeals/prices"
        response = requests.get(url=sheet_endpoint, headers=sheet_headers)
        self.sheet_data = response.json()["prices"]

        user_endpoint = "https://api.sheety.co/b3a71263788566b08e78e5d530defc94/flightDeals/users"
        response = requests.get(url=user_endpoint)
        self.user_data = response.json()["users"]

    def update_row(self, object_id, row):
        edit_endpoint = f"https://api.sheety.co/b3a71263788566b08e78e5d530defc94/flightDeals/prices/{object_id}"
        parameters = {"price": row}
        response = requests.put(url=edit_endpoint, json=parameters, headers=sheet_headers)





# user_endpoint = "https://api.sheety.co/b3a71263788566b08e78e5d530defc94/flightDeals/users"
# response = requests.get(url=user_endpoint)
# user_data = response.json()["users"]
# print(user_data[0]["email"])
