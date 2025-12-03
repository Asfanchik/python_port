# def rectangle (a, b):
#     a = a
#     b = b
#     return a * b
#
# ractangle = rectangle(2, 5)
# print(ractangle)
#
#
# class Book:
#     def __init__(self, name, author):
#         self.name = name
#         self.author = author
#
#     def info(self):
#         return f" Book name is {self.name}, Author is {self.author}"
#
# infor = Book("war", "lenin")
#
# print(infor.info())

# def even_nom(number):
#     return number % 2 ==0
#
# print(even_nom(4))
# print(even_nom(7))

# class StepsCounter:
#     def __init__(self, owner, steps=0):
#         self.owner = owner
#         self.steps = steps
#     def add_steps(self, steps):
#         self.steps += steps
#
#     def get_steps(self):
#         return f"{self.owner} , {self.steps}"
#
# tracker = StepsCounter("Alex")
# tracker.add_steps(100)
# tracker.add_steps(50)
# print(tracker.get_steps())

# def factorial(n):
#     if n < 0:
#         return None
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(fa)

# def sum_of_digits(number):
#     return sum(int(digit) for digit in str(abs(number)))
#
# print(sum_of_digits(123))

# def arithmetic(a, b, c):
#         try:
#
#             if b == "+":
#                 result = a + c
#             elif b == "-":
#                 result = a - c
#             elif b == "*":
#                 result = a * c
#             elif b == "/":
#                 if c == 0:
#                     print("You cant do this ")
#
#                 else:
#                     result = a / b
#             else:
#                 print("you cant do this bc not +-*/")
#             print(f"{a} {b} {c} = {result}")
#         except ValueError:
#             print("invalid Error")
# print(arithmetic(5, "+", 3 ))

# def filter_mul(numbers):
#     return list(filter(lambda x : x % 3 == 0, numbers))
#
# pepe = [3, 5 ,6, 7, 8, 9]
# print(filter_mul(pepe))




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} {self.age} year"

person = Person("Alex", 23)
print(person.introduce())


class Animal:
    def make_sound(self):
        return "kokoy to "
class Cat:
    def make_sound(self):
        return "Myau"
class Dog:
    def make_sound(self):
        return " gav gav"