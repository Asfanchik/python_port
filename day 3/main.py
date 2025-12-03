# number = int(input( "enter number - "))\
#
# if number / 2 == 0:
#     print(" Eto chislo chotnoe.")
# else:
#     print("eto chislo ne chotnoe.")
# number = int(input("enter your hight - "))
#
# if number > 120:
#     print("you can rite rolr")
#     age = int(input("Input your age - "))
#     if age < 12:
#         print("you must pay 5$")
#     elif age <=18:
#         print("you must pay 7$")
#     else:
#         print("you must pay 12$")
# else:
#     print("you can't rite")
# height = float(input("enter your hight - "))
# weight = float(input("enter your weight - "))
#
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"your bmi is {bmi}, you are underweight. ")
# elif bmi < 25:
#     print(f"your bmi is {bmi}, you are normal. ")
# elif bmi < 30:
#     print(f"your bmi is {bmi}, you are overweight. ")
# elif bmi < 35:
#     print(f"your bmi is {bmi}, you are obese . ")
# else:
#     print(f"your bmi is {bmi}, you are critical obese ")
# print("Welcome to Pythone Deliveres")
# size = input("what size pizza do you want ? S, M or L - ")
# pepperoni = input("Do you want pepperoni ? Y or N - ")
# extracheese = input("Do you want extra cheese ? Y or N - ")
#
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extracheese == "Y":
#     bill += 1
# print(f" You must pay ${bill}")
# Love calculator
# print("Welcome to love calculator ")
# name1 = input("Your name ? ")
# name2 = input("Your b/gfriend name ? ")
# # верхняя строка ввод имени
# combinate_name = name1 + name2 # summa dvux imen
# lower_case_string = combinate_name.lower()# delaet bolshie bukvi malenkimi
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
# # schitaet skolko ukazanix bukv v slove
# true = t + r + u + e
#
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
# #------------------------------------------
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
#
# print(f"love score = {love_score}")
# if (love_score < 10 ) or (love_score > 90):
#     print(f"Your love score {love_score}, you both like coke and mentos")
# elif (love_score >=40) and (love_score <= 50):
#     print(f"YOUR SCOR IS {love_score}, you alright together. ")
# else:
#     print(f"Your love score {love_score}")

print("Welome to Tresure island")
print("Your mission find tresure")
choise1 = input('You are before door where you are going ? Type "left" or "right" -').lower()
if choise1 == "left":
    choise2 = input('You are wright, go next level.\nDo you want "swim" or "wait" -').lower()
    if choise2 == "wait":
        choise3 = input("You was wright again.\nSo next, befor you door which kind of door do you enter 'red', 'yellow' or 'green' -").lower()
        if choise3 == "red":
            print("Kongratulation, YOU ARE WOOOON")
        else:
            print("YOU LOSE. GAME OVER")
    else:
        print("Sorry. GAME OVER")
else:
    print("Bad idea. GAME OVER")
