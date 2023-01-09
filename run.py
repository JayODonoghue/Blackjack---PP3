

print("BLACKJACK")


def get_username():
    """
    Get username input from the user.
    A while loop collects data from the user that will be a string
    3 to 10 characters long 
    """
    while True:
        print("Please enter your username\n")
        print("Please make sure username is 3 - 10 characters")

        username = input()

        if len(username) >= 3:
            print(f"Welcome {username}")
            break
            
    return username


get_username()