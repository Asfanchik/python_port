# #Describe Problem
# def my_function():
#     for i in range(1, 21):
#         if i ==20:
#             print("You got it")
# my_function()

#Reproduce the bug
from random import randint
dice_img = [1, 2, 3, 4, 5, 6]
dice_num = randint(1,5)
print(dice_img[dice_num])

# #Play computer 
# year = int(input("What's yor year of birth ?"))
# if year >= 1980 and year < 1994:
#     print("You are melinial")
# elif  year >= 1994:
#     print("You are a Gen Z.")

# # Fix the Errors 
# age = int(input("How old are you ?"))
# if age > 18 :
#     print(f"You can drive at age {age}")
# elif age <= 18:
#     print(f"You can't drive at age {age}") 

# #Print is You Friend 
# page = 0 
# word_per_page = 0
# page = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = page * word_per_page
# print(f"Papers - {page}")
# print(f"Word per page - {word_per_page}")
# print(total_words)

# #Use a Debugger 
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
# mutate([1,2,3,4,5,8,13])

# #Ex1
# number = int(input("Which number do you want to check - "))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# #Ex2
# year = int(input("Which year do you want to check - "))

# if year % 4 ==0:
#     if year % 100 ==0:
#         if year % 400==0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# #Ex3
# for number in range(1, 101):
#     if number % 3 == 0 and  number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
