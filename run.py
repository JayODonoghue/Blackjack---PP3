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
    for card in range(2):
        card = random.choice(deck)
        participant.append(card)
        deck.remove(card)

    return card


def additional_card(deck, participant):
    card = random.choice(deck)
    participant.append(card)
    deck.remove(card)


def cards_total(participant_hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    score = 0
    ace = 0

    for card in participant_hand:
        score += values[card[0]]
        if card[0] == 'A':
            ace += 1

    while score > 21 and ace > 0:
        score -= 10
        ace -= 10

    return score


def check_dealer_hand(dealer_hand):
    show_dealer_card = dealer_hand[1]
    print(show_dealer_card)
    print(dealer_hand)
    dealer_total = cards_total(dealer_hand)
    print(f"Dealer total is - {dealer_total}\n\n-------------")
    
    if user_total == 21 and dealer_total != 21:
        print("Blackjack\nUser wins")
    elif dealer_total == 21 and user_total != 21:
        print("Blackjack\nDealer wins")
    else: 
        while True:
            if dealer_total >= 17:
                print("Dealer stands")
                winning_hand(user_hand, dealer_hand)
                break
            elif dealer_total < 17:
                update_deck = deck()
                additional_card(update_deck, dealer_hand)
                print(dealer_hand[-1])
                new_dealer_total = cards_total(dealer_hand)
                print(new_dealer_total)
                if new_dealer_total > 21:
                    print("dealer has gone bust")
                    break
                elif new_dealer_total == 21:
                    print("Blackjack")
                    winning_hand(user_hand, dealer_hand)
                    break
                elif new_dealer_total >= 17 and new_dealer_total != 21:
                    print("Dealer stands")
                    winning_hand(user_hand, dealer_hand)
                    break


def hit_or_stand():
    while True:
        if user_total == 21:
            check_dealer_hand(dealer_hand)
            break
        elif user_total < 21:
            hit_stand = input("Press [h] to Hit or [s] to Stand -  ")
            if hit_stand.lower() == "h":
                update_deck = deck()
                additional_card(update_deck, user_hand)
                print(user_hand[-1])
                new_user_total = cards_total(user_hand)
                print(new_user_total)
                if new_user_total > 21:
                    print("user has gone bust")
                    break
                elif new_user_total == 21:
                    print("Blackjack")
                    check_dealer_hand(dealer_hand)
                    break
            elif hit_stand.lower() == "s":
                print("check scores & dealer card")
                check_dealer_hand(dealer_hand)
                break
            else:
                print("-------\nInvalid response\n")


def winning_hand(participant1, participant2):
    if cards_total(user_hand) > 21:
        print("dealer wins")
    elif cards_total(user_hand) > cards_total(dealer_hand):
        print("User wins")
    elif cards_total(dealer_hand) > cards_total(user_hand):
        print("Dealer wins")
    elif cards_total(user_hand) == cards_total(dealer_hand):
        print("push")
        

def place_bet():
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
                
        except ValueError:
            print("-------\nInvalid bet type, please try again.\n")
                       
    
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
            place_bet()
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
            place_bet()
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
print("Dealing\n")
clear()
print(f"\nPlayer hand is - {user_hand[0]} , {user_hand[1]}\n")
user_total = cards_total(user_hand)
print(f"Player total is - {user_total}\n\n-------------")
cards_total(user_hand)
print(f"\nDealer hand is - {dealer_hand[0]} , ?")
hit_or_stand()


