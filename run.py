import os
import random
import time
import pyfiglet
from termcolor import cprint


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
    cprint(pyfiglet.figlet_format("\nBLACKJACK\n"), 'red')
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
    Uses the random module to choose the dealers and players cards.
    """
    for card in range(2):
        card = random.choice(deck)
        participant.append(card)
        deck.remove(card)

    return card


def additional_card(deck, participant):
    """
    Once hit is entered by the user this function is called and uses
    the random module to draw an additional card and remove it from deck.
    """
    card = random.choice(deck)
    participant.append(card)
    deck.remove(card)


def cards_total(participant_hand):
    """
    Totals the values of the cards in the participants hand and return the
    score. It also adjusts the value for 'A' accordingly
    """
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
        ace -= 1

    return score


def check_dealer_hand(dealer_hand, user_hand):
    """
    Once called, reveals the dealers full hand and then distinguishes whether
    the dealer will stand or hit. Also takes into account if Blackjack is
    gotten from first hand, or if dealer goes bust once hit.
    """
    if cards_total(user_hand) > 21:
        player_coins.lose_bet()
        go_again()
    else:
        show_dealer_card = dealer_hand[1]
        print(f"Dealer's second card is ... {show_dealer_card}")
        print(f"Dealer's hand is {dealer_hand[0]}, {dealer_hand[1]}")
        dealer_total = cards_total(dealer_hand)
        print(f"\nDealer total is - {dealer_total}\n\n-------------")

    if cards_total(user_hand) == 21 and cards_total(dealer_hand) != 21:
        print("Blackjack")
    elif cards_total(dealer_hand) == 21 and cards_total(user_hand) != 21:
        print("Blackjack")
    elif cards_total(dealer_hand) == 21 and cards_total(user_hand) == 21:
        print("Push")
    else:
        while True:
            if dealer_total >= 17:
                print("Dealer stands")
                break
            elif dealer_total < 17:
                additional_card(update_deck, dealer_hand)
                print(dealer_hand[-1])
                new_dealer_total = cards_total(dealer_hand)
                print(new_dealer_total)
                if new_dealer_total > 21:
                    print("dealer has gone bust")
                    player_coins.win_bet()
                    break
                elif new_dealer_total == 21:
                    print("Blackjack")
                    break
                elif new_dealer_total >= 17 and new_dealer_total != 21:
                    print("Dealer stands")
                    break


def hit_or_stand(user_total, user_hand):
    """
    Gives the user a choice to hit or stand. If 'hit' is chosen, then
    an additional card is called and the total of the dealers hand
    is recalculated. If 'stand' the dealers hand is viewed.
    """
    while True:
        if user_total == 21:
            break
        elif user_total < 21:
            hit_stand = input("Press [h] to Hit or [s] to Stand -  ")
            if hit_stand.lower() == "h":
                additional_card(update_deck, user_hand)
                print(user_hand[-1])
                new_user_total = cards_total(user_hand)
                print(new_user_total)
                if new_user_total > 21:
                    print("User has gone bust.\nDealer wins")
                    player_coins.lose_bet
                    break
                elif new_user_total == 21:
                    print("Blackjack")
                    break
            elif hit_stand.lower() == "s":
                break
            else:
                print("-------\nInvalid response\n")


def winning_hand(user_hand, dealer_hand):
    """
    Compares users hand to dealers and returns who the winner is or
    if a draw/push.
    """
    if cards_total(user_hand) < 21 and cards_total(dealer_hand) < 21:
        if cards_total(user_hand) > cards_total(dealer_hand):
            print("user wins")
            player_coins.win_bet()
        elif cards_total(dealer_hand) > cards_total(user_hand):
            print("dealer wins")
            player_coins.lose_bet()
        elif cards_total(user_hand) == cards_total(dealer_hand):
            print("push")
    elif cards_total(dealer_hand) == 21 and cards_total(user_hand) != 21:
        print("Dealer wins")
        player_coins.lose_bet()
    elif cards_total(user_hand) == 21 and cards_total(dealer_hand) != 21:
        print("User wins")
        player_coins.win_bet()


class Coins:
    """
    Class for all dealings with the coins aspect of the game,
    adding and subtracting the coins after each hand
    """

    def __init__(self):
        self.coins = 1000
        self.bet = 0

    def win_bet(self):
        """
        Adds coins if you win the hand
        """
        self.coins += self.bet

    def lose_bet(self):
        """
        Deducts the coins if you lose the hand.
        """
        self.coins -= self.bet


def go_again():
    """
    Once the winnning hand is determined the user is given the option to play
    again or to quit retirning to the beginning.
    """
    if player_coins.coins == 0:
        print("Awh no more coins, game over. Thanks for playing!")
        time.sleep(3)
        clear()
        player_coins.coins = 1000
        start_up()
    else:
        print("\nWould you like to start play another round?")
        while True:
            round_choice = input("Press [y] to start or [q] to quit - ")

            if round_choice.lower() == "y":
                clear()
                main()
                break
            elif round_choice.lower() == "q":
                clear()
                player_coins.coins = 1000
                start_up()
                break
            else:
                print("-------\nInvalid response\n")

        return round_choice


def place_bet(coins):
    """
    Prints coins value and requests that the player place their bets.
    Betting is limited to multiples of 5 and a minimum bet of 10 is required,
    otherwise a valuerror response is printed.
    """

    print(f"{USERNAME}'s total coins = {coins.coins}\n\n")
    print("Place your bets\n")
    time.sleep(0.5)
    print("A minimum bet of 10 coins per hand is required.")
    print("The player may not place a wager that exceeds their total coins.")
    print("The player's wager must be a number that is a multiple of 5.\n")
    while True:

        try:
            coins.bet = int(input("Place wager - eg 10, 15, 20 -  "))
            if coins.bet < 10:
                print("---\nA minimum bet of 10 coins is required\n")
            elif player_coins.bet > coins.coins:
                print("--\nYou do not have enough funds to place this bet\n")
            elif (coins.bet % 5) != 0:
                print("---\nMust be a multiple of 5\n")
            else:
                print("\nNo more bets")
                time.sleep(0.5)
                clear()
                break
        except ValueError:
            print("-------\nInvalid bet type, please try again.\n")
        continue


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
            break
        elif choice.lower() == "i":
            clear()
            instructions()
            break
        else:
            print("-------\nInvalid response\n")

    return choice


def start_up():
    """
    Starts the whole process. Prints greeting message and calls
    the main function if instructions not chosen.
    """
    global USERNAME
    USERNAME = get_username()
    instructions_choice()
    main()


def main():
    """
    Main function that runs the game by calling all the required functions
    """
    user_hand = []
    dealer_hand = []
    place_bet(player_coins)
    global update_deck
    update_deck = deck()
    deal_cards(update_deck, user_hand)
    deal_cards(update_deck, dealer_hand)
    print("Dealing\n")
    time.sleep(1.0)
    clear()
    print(f"\nPlayer hand is - {user_hand[0]} , {user_hand[1]}")
    user_total = cards_total(user_hand)
    print(f"Player total is - {user_total}\n\n")
    cards_total(user_hand)
    print(f"\nDealer hand is - {dealer_hand[0]} , ?\n\n-------------\n")
    hit_or_stand(user_total, user_hand)
    check_dealer_hand(dealer_hand, user_hand)
    winning_hand(user_hand, dealer_hand)
    go_again()


player_coins = Coins()
start_up()
