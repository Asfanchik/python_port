import requests
from datetime import datetime
import smtplib

MY_LAT = 37.20682000
MY_LONG = 126.81690000

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

# response = requests.get(url="https://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_positions"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted": 0,
}

reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
reponse.raise_for_status()
data = reponse.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]



print(sunrise)
print((sunset))

time_now = datetime.now()

if time_now == sunset:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        x = connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Wake up\n\n{time_now}"
        )

print(time_now)