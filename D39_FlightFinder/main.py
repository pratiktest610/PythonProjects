from sheet_manager import SheetManager
from flight_manager import FlightManager
from flight_data import FlightData
from mail_manager import MailManager

sheet_manager = SheetManager()
flight_manager = FlightManager()
mail_manager = MailManager()


def update_iata():
    object_id = 1
    for row in sheet_manager.sheet_data:
        object_id += 1
        city = row["city"]
        row["iataCode"] = flight_manager.iata_code(city)
        sheet_manager.update_row(object_id, row)


def main():
    for row in sheet_manager.sheet_data:
        code = row["iataCode"]
        price = row["price"]
        if flight_manager.search(code):
            flight_data = FlightData(flight_manager.data)
            if flight_data.price <= price:
                print(flight_data.msg)
                for user in sheet_manager.user_data:
                    email = user["email"]
                    mail_manager.send_email(flight_data.msg, email)


# update_iata()
main()



