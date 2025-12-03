# file = open("hello.txt") / with open("hello.txt") as file
# contents = file.read()
# print(contents)
# file.close() #nujen dlya ne zapolneniya pamyati. Obichnoe otkrie


with open("hello.txt", mode="w") as file:
    file.write("Alex")