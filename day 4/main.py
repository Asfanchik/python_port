import random
# random_intager = random.randint(1, 3)
# print(random_intager)
#random.seed(23)

#randomIntegeter = random.randint(1, 10)
#print(randomIntegeter)

#randomFloat = random.random() * 5
#print(randomFloat)
# test_seed = int(input("Create a seed: "))# введите число  
# random.seed(123)#часть для упровления рандомом
# random_side = random.randint(0, 1)# сам рандомизатор
# if random_side == 1:
#     print("Head")
# else:
#     print("Tail")

# state_of_america = ["Delavera", "Pennsilvania", "New Jersiy", "Georgia", "Conecticut", "Marryland", "South Corolina", "Virginia"]
# #сарая инфа
# state_of_america.append("Angela", "ton")
# #добовляет нов инфу в сарую
# print(state_of_america)
#
# test_seed = int(input("Create a seed number: "))
# nameAsCSV = input("Give me everybadyname - ")
# names = nameAsCSV.split()
# # num_items = len(names)#анадизирует число людей
# # random_choice = random.randint(0, num_items - 1)#Генерирует числа между 0 и последним индексом
# # person_who_will_pay = names[random_choice]

# person_who_will_pay = random.choices(names)
# print(f"Today pay for meals - {person_who_will_pay}")

# row1 = ["_","_","_"]
# row2 = ["_","_","_"]
# row3 = ["_","_","_"]
# #колоны
# map = [row1, row2, row3]
# print("{row1}\n{row2}\n{row3}")
# position = input("Write do you want to put tresure ? ")
# horizontal = int(position[0])
# vertical = int(position[1])
# #позиции колон
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"
# # функция выбора колон
# print(f"{row1}\n{row2}\n{row3}")# выводить ответ

rock = "ROCK"
papper = "PAPPER"
scissors = "SCISSORS"
# камен нож бум
game_list = [rock, papper, scissors]# лист для определения числа слов

user_choice = int(input("What do you choose ? Type 0-2, 0 - Rock, 1 - Papper, 2 - Scissors\n"))

print(game_list[user_choice])
computer_choice = random.randint(0, 2)
print("Computer choose ")
print(game_list[computer_choice])#распределяет числа на лист

if user_choice >=3 or user_choice <0:
    print("Error")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice ==2:
    print("You lose") 
elif user_choice == computer_choice:
    print("It's draw")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!") #паравила игры
