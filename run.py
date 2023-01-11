import os


def clear():
    os.system('clear')


def get_username():
    """
    Get username input from the user.
    A while loop collects data from the user that will be a string
    3 to 10 characters long 
    """
    print("\nBLACKJACK\n")
    print("Please make sure your username is 3 - 10 characters")

    while True:    
        username = input("Please enter your username - ")

        if len(username) >= 3 and len(username) < 11:
            print(f"\nWelcome {username}!")
            break
        else:
            print("-------\nInvalid username, 3-10 characters required")

    return username


def start_game():
    coins = 1000
    print(f"{username}'s total coins = {coins}\n\n")
    print("Place your bets\n")
    print("A minimum bet of 10 coins per hand is required.")
    print("The player may not place a wager that exceeds their total coins.")
    print("The player's wager must be a number that is a multiple of 5.\n")
    while True:
        try:
            wager = input("Place wager - eg 10, 15, 20 -  ")
            wager = int(wager)

            if wager < 10:
                print("A minimum bet of 10 coins is required")
            elif wager > coins:
                print("You do not have enough funds to place this bet")
            elif wager % 5 == 0:
                print("Must be a multiple of 5")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
    

def instructions():
    print("\nInstructions\n")
    print("Step 1: Put down your bet\n")
    print("")
    print("Step 2: Get your cards dealt\n")
    print("Step 3: Decide when you want to 'hit' or 'stand'\n")
    print("Step 4(a): 'Hit'\n")
    print("Step 4(b): 'Stand'\n")
    print("Step 5: Understand the opponent's hand\n")
    print("Step 6: The outcome\n")
    print("Would you like to start the game?")
    while True:
        start = input("Press [s] to start or [r] to return to main menu -  ")

        if start == "s":
            clear()
            start_game()
            break
        elif start == "r":
            clear()
            get_username()
            instructions_choice()
            break
        else:
            print("-------\nInvalid response\n")
    
    return start


def instructions_choice():
    print("\nWould you like to start game or read instructions?")

    while True:
        choice = input("Press [s] to start or [i] to view instructions - ")

        if choice == "s":
            clear()
            start_game()
            break
        elif choice == "i":
            clear()
            instructions()
            break
        else:
            print("-------\nInvalid response\n")
    
    return choice


username = get_username()
instructions_choice()
