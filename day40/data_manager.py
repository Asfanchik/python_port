import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/063ef0dd3067584188b178e17151a7b4/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self.price_endpoint = os.environ["PRICE_ENDPOINT"]
        self.users_endpoint = os.environ["USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.custumer_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_custumer_emails(self):
        response = requests.get(url=self.users_endpoint)
        response.raise_for_status() # that shows errors
        data = response.json() # transformed JSON to python dict
        self.custumer_data = data["users"]
        return self.custumer_data # return list of users in sheet
