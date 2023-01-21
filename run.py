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
        username = input("Please enter your username - \n")

        if len(username) >= 3 and len(username) < 11:
            cprint(f"\nWelcome {username}!", 'blue')
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
        print(f"\nDealer's second card is ... {show_dealer_card}")
        print(f"Dealer's hand is {dealer_hand[0]}, {dealer_hand[1]}")
        dealer_total = cards_total(dealer_hand)
        cprint(f"Dealer total is - {dealer_total}\n", 'yellow')

    if cards_total(user_hand) == 21 and cards_total(dealer_hand) != 21:
        print("\nBlackjack")
    elif cards_total(dealer_hand) == 21 and cards_total(user_hand) != 21:
        print("\nBlackjack")
    elif cards_total(dealer_hand) == 21 and cards_total(user_hand) == 21:
        cprint("\nPush", 'green')
    else:
        while True:
            if dealer_total >= 17:
                print("\nDealer stands")
                break
            elif dealer_total < 17:
                additional_card(update_deck, dealer_hand)
                print(f"Dealer draws {dealer_hand[-1]}")
                new_dealer_total = cards_total(dealer_hand)
                cprint(f"Dealer total is - {new_dealer_total}\n", 'yellow')
                if new_dealer_total > 21:
                    print("\nDealer has gone bust")
                    cprint("User wins", 'green')
                    player_coins.win_bet()
                    break
                elif new_dealer_total == 21:
                    print("\nBlackjack")
                    break
                elif new_dealer_total >= 17 and new_dealer_total != 21:
                    print("\nDealer stands")
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
            hit_stand = input("Press [h] to Hit or [s] to Stand -  \n")
            if hit_stand.lower() == "h":
                additional_card(update_deck, user_hand)
                print(f"\n{USERNAME} draws {user_hand[-1]}")
                new_user_total = cards_total(user_hand)
                cprint(f"Player total is - {new_user_total}\n", 'yellow')
                if new_user_total > 21:
                    print("User has gone bust")
                    cprint("Dealer wins", 'green')
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
            cprint("User wins", 'green')
            player_coins.win_bet()
        elif cards_total(dealer_hand) > cards_total(user_hand):
            cprint("Dealer wins", 'green')
            player_coins.lose_bet()
        elif cards_total(user_hand) == cards_total(dealer_hand):
            cprint("Push", 'green')
    elif cards_total(dealer_hand) == 21 and cards_total(user_hand) != 21:
        cprint("Dealer wins", 'green')
        player_coins.lose_bet()
    elif cards_total(user_hand) == 21 and cards_total(dealer_hand) != 21:
        cprint("User wins", 'green')
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
        cprint("\nNo more coins. Thanks for playing!", 'red')
        time.sleep(2.5)
        clear()
        cprint(pyfiglet.figlet_format("\nGOODBYE!"), 'red')
        time.sleep(2)
        clear()
        player_coins.coins = 1000
        start_up()
    else:
        print("\nWould you like to start play another round?")
        while True:
            round_choice = input("Press [y] to start or [q] to quit - \n")

            if round_choice.lower() == "y":
                clear()
                main()
                break
            elif round_choice.lower() == "q":
                cprint("\nThanks for playing!", 'red')
                time.sleep(1.5)
                clear()
                cprint(pyfiglet.figlet_format("\nGOODBYE!"), 'red')
                time.sleep(2)
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

    cprint(f"{USERNAME}'s total coins = {coins.coins}\n\n", 'blue')
    cprint("Place your bets\n", 'light_red')
    time.sleep(0.5)
    print("A minimum bet of 10 coins per hand is required.")
    print("The player may not place a wager that exceeds their total coins.")
    print("The player's wager must be a number that is a multiple of 5.\n")
    while True:

        try:
            coins.bet = int(input("Place wager - eg 10, 15, 20 -  \n"))
            if coins.bet < 10:
                print("---\nA minimum bet of 10 coins is required\n")
            elif player_coins.bet > coins.coins:
                print("--\nYou do not have enough funds to place this bet\n")
            elif (coins.bet % 5) != 0:
                print("---\nMust be a multiple of 5\n")
            else:
                cprint("\nNo more bets\n", 'light_red')
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
    cprint("\nInstructions\n", 'cyan')
    print("Step 1: Put down your bet.")
    print("First of all, place your wager. This wager must be a multiple"
          " of five and be a minimum of 10 coins")
    print("\nStep 2: Get your cards dealt.")
    print("You are dealt 2 cards and shown your total. However only"
          " one of the dealers card is shown and one is hidden"
          " Please note that an ace can be valued at 1 or 11 depending"
          " on your total, if you exceed 21 and have an ace it will be 1,"
          " otherwise it wil be 11")
    print("\nStep 3: Decide when you want to 'hit' or 'stand'.")
    print("You will then be given the option to stay on the total you have"
          "or to hit and draw another card")
    print("\nStep 4(a): 'Hit'.")
    print("Another card is added and your new total is calculated")
    print("\nStep 4(b): 'Stand'.")
    print("Stay with the total you have. Reveal dealer's second card")
    print("\nStep 5: Understand the opponent's hand")
    print("The dealer's total is calculated. If the dealer's total is under 17"
          " then the dealer will automatically have to hit. If the dealer is"
          " between 17 and 21 the dealer stands")
    print("\nStep 6: The outcome.")
    print("The aim of the game is to get as close to 21 as possible. If either"
          " the user of dealer go over 21 its bust. Which means the other"
          " player wins. If someone gets 21 its Blackjack and the opponents"
          " hand is compared. If the totals are equal to each other it's a"
          " push (which means draw). If both players are below 21 then it"
          " simply comes down to whoever has the highest total.")
    print("Would you like to start the game?")
    while True:
        start = input("Press [s] to start or [r] to return to main menu -  \n")

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
        choice = input("Press [s] to start or [i] to view instructions - \n")

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
    cprint(pyfiglet.figlet_format("Dealing\n"), 'green')
    time.sleep(1.0)
    clear()
    print(f"\nPlayer hand is - {user_hand[0]} , {user_hand[1]}")
    user_total = cards_total(user_hand)
    cprint(f"Player total is - {user_total}\n\n", 'yellow')
    cards_total(user_hand)
    print(f"\nDealer hand is - {dealer_hand[0]} , ?\n\n-------------\n")
    hit_or_stand(user_total, user_hand)
    check_dealer_hand(dealer_hand, user_hand)
    winning_hand(user_hand, dealer_hand)
    go_again()


player_coins = Coins()
start_up()
