#Date for questions
date = [{
    'name' : 'Instogram',
    'follower_count' : 619,
    'description' : 'social media platform',
    'country' : 'U.S.'
},
{
    'name' : 'Cristiano Ronaldo',
    'follower_count' : 563,
    'description' : 'footbal player',
    'country' : 'Portugalia'
},
{
    'name' : 'Leo Messi',
    'follower_count' : 443,
    'description' : 'footbal player',
    'country' : 'Argentina'
},
{
    'name' : 'Selena Gomez',
    'follower_count' : 401,
    'description' : 'singer',
    'country' : 'U.S.'
},
{
    'name' : 'Kylie Jenner',
    'follower_count' : 382,
    'description' : 'Bissneswoman',
    'country' : 'U.S'
}
]

import random
#from replit import clear


def format_date(account):
    """Format the account date into printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
score = 0
game_should_continue = True
account_b = random.choice(date)

#Make the game repeatable.
while game_should_continue:
            
    #Generate a random accounta from the game date.
    
    #Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(date)
    while account_a == account_b:
        account_b = random.choice(date)

    print(f"Compare A: {format_date(account_a)}.")
    print("VS")
    print(f"Compare B: {format_date(account_b)}.")

    #Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Check if user is correct.

    #Get follower count of each account.
    a_follow_count = account_a["follower_count"]
    b_follow_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follow_count, b_follow_count)

    #Clear the feedback on their guess
    #clear()
    #Give user feedback on their guess.

    #Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Filanl score: {score}")
         
