#FileNotFound
# with open("a-file.txt") as file:
#   file.read()

#Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_exist"]

#Index Error
# fruit = ["Apple", "Pearle", "Banana"]
# fruit = fruit_list[3]




# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key{error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")



hight = float(input("hight = "))
weight = int(input("weight = "))

if hight >3:
    raise ValueError("humond hight can't be hight 3")

bmi = weight / hight ** 2

