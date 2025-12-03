from dotenv import load_dotenv # for get login and password
import requests
import os # for working whith file
from requests.auth import HTTPBasicAuth # for site to say "This my password and login "

load_dotenv() # to get from .env file login and password

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/063ef0dd3067584188b178e17151a7b4/flightDeals/prices"



class DataManager:

    def __init__(self): # this function get login and password enter to site after create folder for ticket
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}


    def get_destination_date(self): # function "give me tickets
        # Use the Sheety API to Get all the data in that sheet and print it out. 
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data =response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self): # function for updating price
        for city in self.destination_data:
            # take the code of city and put to folder price
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            # send updates to site
            response = requests.put(
                url = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json= new_data,
                auth=self._authorization
            )
            print(response.text)