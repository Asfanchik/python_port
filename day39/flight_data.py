class FlightData:
   def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
       # give information abaut flights
       self.price = price
       self.origin_airport = origin_airport
       self.destination_airport = destination_airport
       self.out_date = out_date
       self.return_date = return_date

def find_cheapest_flight(data):
       # get "data" - inform abaut flights, and return cheapet flight
    if data is None or not data['data']:
        print("No flight")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")


    first_flight = data['data'][0] # get frist flight from "data"
    lowest_price = float(first_flight["price"]["grandTotal"]) # get price ("grandTotal")
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0] # get iataCode departure and arriv
    return_data = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0] # date return get and cut to YYYY-MM-DD format

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_data) # current cheap ticket

    for flight in data["data"]:# searching more cheapest
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_data = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_data)
            print(f"Lowest price to {destination} is ${lowest_price}")

    return cheapest_flight # return after searching cheap
