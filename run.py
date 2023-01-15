import os
import random

user_hand = []
dealer_hand = []


def clear():
    """
    Clears the screen once called.
    """
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


def deck():
    """
    Creates a deck of cards by iterating through the lists of suits and ranks 
    to accumulate a deck.
    """
    deck = []
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for suit in suits:
        for rank in ranks:
            deck.append(rank + " " + suit)
    
    return deck


def deal_cards(deck, participant):
    """
    Prints 'dealing' and uses the random module to choose the dealers
    and players cards. It also totals the values of the cards of the
    each player along with giving them the choice of input hit/stand
    """
    print("Dealing\n")

    for card in range(2):
        card = random.choice(deck)
        participant.append(card)
        deck.remove(card)

    return card


def cards_total(participant_hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    score = 0

    for user_card in user_hand:
        score += values[user_card[0]]
    
    print(score)


def start_game():
    """
    Prints coins value and requests that the player place their bets.
    Betting is limited to multiples of 5 and a minimum bet of 10 is required,
    otherwise a valuerror response is printed.
    """
    coins = 1000
    print(f"{username}'s total coins = {coins}\n\n")
    print("Place your bets\n")
    print("A minimum bet of 10 coins per hand is required.")
    print("The player may not place a wager that exceeds their total coins.")
    print("The player's wager must be a number that is a multiple of 5.\n")
    while True:
        wager = input("Place wager - eg 10, 15, 20 -  ")
        try:
            wager = int(wager)

            if wager < 10:
                print("---\nA minimum bet of 10 coins is required\n")
            elif wager > coins:
                print("--\nYou do not have enough funds to place this bet\n")
            elif (wager % 5) != 0:
                print("---\nMust be a multiple of 5\n")
            else:
                print("No more bets")
                clear()
                update_deck = deck()
                deal_cards(update_deck, user_hand)
                deal_cards(update_deck, dealer_hand)
                return wager
                
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
                       
    
def instructions():
    """
    Lists out instructions and gives user choice to play
    or return to home screen, provided correct data in inputted.
    """
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

        if start.lower() == "s":
            clear()
            start_game()
            break
        elif start.lower() == "r":
            clear()
            get_username()
            instructions_choice()
            break
        else:
            print("-------\nInvalid response\n")
    
    return start


def instructions_choice():
    """
    Gives user option to start game or read instructions.
    Data is inputted by user once correct conditions are met.
    """
    print("\nWould you like to start game or read instructions?")

    while True:
        choice = input("Press [s] to start or [i] to view instructions - ")

        if choice.lower() == "s":
            clear()
            start_game()
            break
        elif choice.lower() == "i":
            clear()
            instructions()
            break
        else:
            print("-------\nInvalid response\n")
    
    return choice


username = get_username()
instructions_choice()
print(f"Player hand is - {user_hand[0]} , {user_hand[1]}")
cards_total(user_hand)
print(f"\n\nDealer hand is - {dealer_hand[0]} , ?")
show_dealer_card = print(dealer_hand[1])

