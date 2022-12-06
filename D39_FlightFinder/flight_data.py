class FlightData:

    def __init__(self, data: dict):

        try:
            self.flag = data["data"][0]["route"][1]
            self.x = 1
            self.depart = data["data"][0]["route"][0]['local_departure'].split("T")[0]
            self.arrival = data["data"][0]["route"][1]['local_arrival'].split("T")[0]
            self.city_from = data["data"][0]["route"][0]['cityFrom']
            self.city_to = data["data"][0]["route"][1]['cityTo']
            self.price = data["data"][0]["price"]
            self.via_city = data["data"][0]["route"][0]['cityTo']
            self.msg = f"Subject:LOW PRICE ALERT!!\n\nFly to {self.city_to} from {self.city_from}" \
                       f" via {self.via_city} at only Rs.{self.price}." \
                       f"Depart on {self.depart}" \
                       f" and reach by {self.arrival}"
            

        except IndexError:
            self.x = 0
            self.depart = data["data"][0]["route"][0]['local_departure'].split("T")[0]
            self.arrival = data["data"][0]["route"][0]['local_arrival'].split("T")[0]
            self.city_from = data["data"][0]["route"][0]['cityFrom']
            self.city_to = data["data"][0]["route"][0]['cityTo']
            self.price = data["data"][0]["price"]
            self.msg = f"Subject:LOW PRICE ALERT!!\n\nFly to {self.city_to} from {self.city_from}" \
                  f" at only Rs.{self.price}." \
                  f"Depart on {self.depart}" \
                  f" and reach by {self.arrival}"
