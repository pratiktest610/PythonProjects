from data_manager import *
from flight_search import *
from flight_data import CompareFlightData

data_manager = DataManager()
flight_search = FlightSearch()
cities = data_manager.get_cities()
try:
    codes = data_manager.get_codes()
except:
    codes = flight_search.get_codes(cities)
    data_manager.load_codes(codes)


flight_search.search_flight(codes)
# CompareFlightData(data_manager.rows, flight_search.data)
