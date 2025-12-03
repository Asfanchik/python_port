# import requests
##Task1
# url = "https://api.quotable.io/random"
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json() # transform json answer to Python object
#     print(f"Цитата: \"{data['content']}\"")
#     print(f"Автор: {data['author']}")
# else:
#     print("Ошибка при получении цитаты:", response.status_code)
import requests

#Task 2

# url = "http://api.open-notify.org/iss-now.json"
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json() # transform json answer to Python object
#
#     position = data["iss_position"] #selct in dictionary in data
#     print(f"longat: \"{position['longitude']}\"")
#     print(f"latatude: {position['latitude']}")
# else:
#     print("Ошибка при получении:", response.status_code)




# #Task 3
# url = "https://dog.ceo/api/breeds/image/random/5"
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()
#
#     position = data["message"]
#     print(f" 1-phto = {position[0]}")
#     print(f" 2-phto = {position[1]}")
#     print(f" 3-phto = {position[2]}")
#     print(f" 4-phto = {position[3]}")
#     print(f" 5-phto = {position[4]}")
#
# else:
#     print("Ошибка при получении:", response.status_code)

#task 4
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "Heloo Api",
#     "body":"I want say something",
#     "userid": 1
# }
#
#
# response = requests.post(url, json=data)
# print(" Answer:", response.json())
#



# #task 5
# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.delete(url)
#
# print("Answer: ", response.status_code)
# print(response.text)

# task6
# city ="Seoul"
# url = f"https://wttr.in/{city}?format = 3"
#
# response = requests.get(url, )
# print(response.text)


#Asisstant
weather_city = "Hwaseong"
url_weather = f"https://wttr.in/{weather_city}?format=3"

response = requests.get(url_weather)
print("Wearher is ", response.text)

fact_url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
response_fact = requests.get(fact_url)

if response_fact.status_code == 200:
    data = response_fact.json()

    fact = data["text"]
    print(f"Today fact: {fact}")
else:
    print("Error")

dog_url = "https://dog.ceo/api/breeds/image/random/5"
response_dog = requests.get(dog_url)

if response_dog.status_code == 200:
    data_dog = response_dog.json()

    dog = data_dog["message"]
    print(f"dog_photo {dog[0]}")
