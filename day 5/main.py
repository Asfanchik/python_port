# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "Pie")

# student_heights = input("list of students hights ->").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# number_of_students = 0
# for student in student_heights:
#     number_of_students +=1

# average_height = round(total_height / number_of_students)
# print(average_height)

# student_score =  input("Input list of students ")
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])
# print(student_score)


# highest_score = 0 
# for score in student_score:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")
# total = 0
# for number in range(2, 101, 2):
#      total += number
#      print(total)
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 ==0:
#         print("Fizz")
#     elif number % 5 ==0:
#         print("Buzz")
#     else:
#         print(number)
# Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
print("Welcome to my password generator")
nr_letters = int(input("How many letters would you like in your password\n"))
nr_symbols = int(input(f"How many symbols would you like\n"))
nr_numbers = int(input(f"How many number would you like \n"))
password_list = []
 
 #EASy level
for char in range (1, nr_letters + 1):
    password_list += random.choice(letters)
    
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(number)
    
    
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char

print(f"Your password {password}")
