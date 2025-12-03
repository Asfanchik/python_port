# Function with output

# def format_name(f_name, l_name):
#     if f_name =="" or l_name == "":
#         return 'You dont enter'
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("Enter what is your f name- "), input("Enter your l name- ")))
# ch1
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
        
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
# year = int(input("Enter a year- "))
# month = int(input("Enter a month- "))
# days = days_in_month(year, month)
# print(days)

# Already used function with outputs
#

#Return as an early edit
# def format_name(f_name, l_name):
#     """Take a first and last name and 
#     format it to return the 
#     title case version of the name"""
#     if f_name == "" or l_name == "":
#         return "you didn't provide valid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Results: {formated_f_name} {formated_l_name}"
# format_name()

# Calculator 
# Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

opiration = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("what's the first number: "))
    for symbol in opiration:
        print(symbol)
    should_contunue = True    
    while should_contunue:
        opiration_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("what's the second number: "))
        calculation_function = opiration[opiration_symbol]
        answer = calculation_function(num1, num2)


        print(f"{num1} {opiration_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a : ") == "y":
            num1 = answer
        else:
            should_contunue = False
            calculator()
calculator()

# operation_symbol = input("Pick an operation: ")
# num3 = int(input("What's the next number: "))

# calculation_function = opiration[operation_symbol]

# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
