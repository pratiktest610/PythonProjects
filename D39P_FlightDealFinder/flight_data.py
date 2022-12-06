class CompareFlightData:
    def __init__(self, sheet_data: list, flight_data: list):
        for i in range(len(sheet_data)):
            if sheet_data[i]["lowestPrice"] >= flight_data[i]["lowestPrice"]:
                print(flight_data[i])

