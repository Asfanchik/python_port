print("Welome to Tresure island")
print("Your mission find tresure")
choise1 = input('You are before door where you are going ? Type "left" or "right" -').lower()
if choise1 == "left":
    choise2 = input('You are wright, go next level.\nDo you want "swim" or "wait" -').lower()
    if choise2 == "wait":
        choise3 = input("You was wright again.\nSo next, befor you door which kind of door do you enter 'red', 'yellow' or 'green' -").lower()
        if choise3 == "red":
            print("Kongratulation, YOU ARE WOOOON")
        else:
            print("YOU LOSE. GAME OVER")
    else:
        print("Sorry. GAME OVER")
else:
    print("Bad idea. GAME OVER")
