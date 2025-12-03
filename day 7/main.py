# word_list = ["ardvark", "baboon", "camel"]
# # list slov
# import random
# choosen_word = random.choice(word_list)
# # randomizator
# guess = input("Guess a letter: ").lower()
# # vvod slova
# for letter in choosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
# opredelitel pravelno li slovo bilo napisono


import random
word_list = ["ardvark", "baboon", "camel"]# list slov
chosen_word = random.choice(word_list)# randomizator
word_length = len(chosen_word) #podshot slov

stages = ['-6','-5','-4','-3','-2','-1'] # ochko jizni

end_of_game = False
lives = 6 #chislo jizney

print(f"Passt, the solution is {chosen_word}.")

display = []# vivodit pustoy list
for _ in range(word_length):
    display += "_"# pechataet proportsionalno kolichestvu slov "_"
print(display)
while not end_of_game:

    guess = input("Guess a latter: ").lower()

    if guess in display:
      print(f"You alredy guessed {guess}")

    for position in range(word_length):# proverayet est li bukvi v slove
        letter = chosen_word[position]
        #print(f"Curren position: {position}\n Current letter : {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter # esli slovo pravelnoe pechataet eto slovo
    print(display)
    if guess not in chosen_word:
        print(f"You gussed {guess}, that is not in the word. You lose life")
        lives -= 1  # otnimaet jizni
        if lives == 0:
            end_of_game = True
            print("You lose")

        print(display)

        if "_" not in display:
            end_of_game = True
            print("YOU WIN")

        print(stages[lives]) # otsilaet k ochku jizney
