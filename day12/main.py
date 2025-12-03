# enemy = 1

# def increase_enemies():
#     global enemy
#     enemy += 1
#     print(f"enemies inside function: {enemy}")
    
# increase_enemies()
# print(f"enemies inside function: {enemy}")

from random import randint


Easy_level = 10
Hard_level = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """check answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


#Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return Easy_level
    else:
        return Hard_level
    
    
def game():       
#CHoose a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    #print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()
#Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
    
#Let the user guess a number.
        guess = int(input("Make a guess:"))
    
    #Track the number of turns and redice by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if  turns == 0:
            print(f"You've run out of guesses, you lose.The answer was {answer}")
            return
        elif guess != answer:
            print("Guess again.")

game()
  
