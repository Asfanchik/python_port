import os
from datetime import datetime
import requests
from dotenv import load_dotenv
load_dotenv(
)

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"] # get api key from Amadeus
        self._api_secret = os.environ["AMADEUS_SECRET"] # get secret key
        self._token = self._get_new_token() # request access token

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/ x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret' : self._api_secret

        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body) # send request to get token

        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token'] # return token and output to consol token
    def get_destination_code(self, city_name):  # get IATA code aeroport on name
        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url= IATA_ENDPOINT,
            headers = headers ,
            params = query
        ) # send GET request with token and paremetrs search

        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode'] # Try get IATA code from answer
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found " # process Errors if code not found
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults":1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",

        }
        response = requests.get(
            url = FLIGHT_ENDPOINT,
            headers=headers,
            params=query,

        )

        if response.status_code != 200:
            print(f"check flights() response code: {response.status_code}")
            print("There was a probelm with the flight search. \n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-setvice/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()

