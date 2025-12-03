# import requests
#
# API_KEY = "a40f695448eaa2a999044ad84e554bf2"
# App_ID = "89801ee6"
# endpoint_food = "https://trackapi.nutritionix.com/v2/natural/nutrients"
#
# headers = {
#     "x-app-id" : App_ID,
#     "x-app-key": API_KEY,
#     "Content-Type": "application/json"
# }
#
# food_input = input("What kind of food you ate ?")
#
# parameters = {
#     "query" :food_input
# }
#
# response = requests.post(endpoint_food, json=parameters, headers=headers)
# data = response.json()
#
# total_calories = 0
#
# for item in data["foods"]:
#     name = item["food_name"].title()
#     calories = item["nf_calories"]
#     serving = item["serving_qty"]
#     unit = item["serving_unit"]
#
#     print(f"{serving} {unit} {name} - {calories}ccal")
#     total_calories += calories
#
# print(f"\ntotal calories is {total_calories:.2f} ccal")

# import requests
# from datetime import datetime
#
# sheet_endpoint = "https://api.sheety.co/063ef0dd3067584188b178e17151a7b4/toDoList/лист1"
# tasks = []
#
# task_name = input("Enter your task - ")
# duration = input("Enter a time ")
#
# task = {
#     "task": task_name,
#     "duration": duration
# }
# tasks.append(task)
#
#
#
# today_date = datetime.now().strftime("%Y%m%d")
# now_date = datetime.now().strftime("%x")
#
# for item in tasks:
#     sheet_inputs = {
#         "лист1":{
#             "date" : today_date,
#             "task": item["task"],
#             "duration": item["duration"]
#         }
#     }
#     sheet_response = requests.post(sheet_endpoint, json = sheet_inputs)
#     print(sheet_response.text)
#     print(sheet_response.status_code)

import requests
from datetime import datetime, timedelta

sheet_endpoint = "https://api.sheety.co/063ef0dd3067584188b178e17151a7b4/toDoList/лист1"

sleep_str = input("Enter your sleep  time - ")
wake_str = input("Enter your wake up time - ")
sleep = datetime.strptime(sleep_str, "%H:%M").time()
wake = datetime.strptime(wake_str, "%H:%M").time()

today = datetime.now().date()
sleep_datetime = datetime.combine(today, sleep)
wake_datetime = datetime.combine(today, wake)

if wake_datetime < sleep_datetime:
    wake_datetime += timedelta(days=1)

duration = wake_datetime - sleep_datetime
duration_hours = round(duration.total_seconds() / 3600, 2) # okruglaet chasi v ponyatnie(8:30 -> 8.5
print(duration_hours)





today_date = datetime.now().strftime("%Y%m%d")
now_date = datetime.now().strftime("%x")

sheet_inputs = {
    "лист1":{
        "date" : today_date,
        "duration": duration_hours
    }
}
sheet_response = requests.post(sheet_endpoint, json = sheet_inputs)
print(sheet_response.text)
print(sheet_response.status_code)