MENU = {
 "esspresso":{
     "ingredients":{
         "water": 50,
         "coffee": 18,
     },
     "cost":1.5,
 },
   "latte":{
     "ingredients":{
         "water": 200,
         "coffee": 24,
         "milk": 150,
     },
     "cost":2.5,
 },
   "cappuccino":{
     "ingredients":{
         "water": 250,
         "coffee": 24,
         "milk": 100,
     },
     "cost":3.0,
 } 
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_ingredients(order_ingredients):
    """This function check ingridients. if ingridients enought print True and not enought print False"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry we don't have needed resources")
            return  False
    return True

def process_coins():
    """THIS function totalize your many"""
    print("How much coins do you have?")
    total = int(input("How many 25 cents do you have?"))*0.25
    total += int(input("How many 10 cents do you have?"))*0.1
    total += int(input("How many 5 cents do you have?"))*0.5
    total += int(input("How many 1 cents do you have?"))*0.1
    return total

def succesful_transaction(money_recived, cost_drink):
    """This function check how many do you have if your many enought print True, if not print Falese"""
    if money_recived >= cost_drink:
        changes = round(money_recived - cost_drink, 2)
        print(f"You have {changes}$ is changes")
        global profit
        profit += cost_drink
        return True
    else:
        print("You don't have a enought money")
        return False

def make_coffee(drink_name, order_ingridients):
    """This function takes away from ordered ingridients"""
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
        print(f"Your drink is {drink_name}. Enjoy it")
        return True
    
#Apparate is on or off
is_on = True
#Prompt user by asking "what would you like?"
while is_on:
    
    order = input("What would you like ? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money {profit}$")
    else:
        drink = MENU[order]
        if check_ingredients(drink["ingredients"]):
            coins = process_coins()
            if succesful_transaction(coins, drink["cost"]):
               make_coffee(order, drink["ingredients"])
        
