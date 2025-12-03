import requests
from datetime import datetime
import os


App_ID = os.environ["ENV_NIX_APP_ID"]
Application_Key = os.environ["NT_API_KEY"]
GENDER = "male"
Weight_kg = 98
Height_sm = 178
age = 23



endpoint_exercise = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

exercise_input = input("What you did do _ ")

headers = {
    "x-app-id" : App_ID,
    "x-app-key": Application_Key,
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg" : Weight_kg,
    "height_cm": Height_sm,
    "age" : age,

}

response = requests.post(endpoint_exercise, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d%m%Y")
now_date = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

for exercise in result["exercises"]:
    sheet_input = {
        "лист1" : {
            "date": today_date,
            "time": now_date,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_input)
    print(sheet_response.text)