import time
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from data_manager import DataManager
from flight_search import FlightSearch

#============= Set up the Flight Search ==============
data_manager = DataManager()
sheet_data = data_manager.get_destination_date() # get list with city
flight_search = FlightSearch()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"


# =============== Update the Airport Codes in Google Sheet ============
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2) # search code IATA
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data # renew list with city
data_manager.update_destination_codes() # save new list with city

# ================ Search for Flights ======================

tomorrow = datetime.now() + timedelta(days=1) # tomorrow daytime
six_month_from_today = datetime.now() + timedelta(days=( 6* 30)) # date after 6 month

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...") # printin information about searching
    flights = flight_search.check_flights( # function which searchin flights from city
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow, # searching date from... to...
        to_time=six_month_from_today
    )
    cheapest_flight= find_cheapest_flight(flights)
    print(f"{destination['city']} : $ {cheapest_flight.price}") # function which choosing chieapest flights from list
    #slowing down request to avoid rate limit
    time.sleep(2)

