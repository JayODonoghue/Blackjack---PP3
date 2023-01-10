

print("\nBLACKJACK\n\n")


def get_username():
    """
    Get username input from the user.
    A while loop collects data from the user that will be a string
    3 to 10 characters long 
    """
    while True:
        print("Please make sure your username is 3 - 10 characters")

        username = input("Please enter your username - ")

        if len(username) >= 3 and len(username) < 11:
            print(f"\nWelcome {username}")
            break
        else:
            print("Invalid username, please make is between 3-10 characters")

    return username


get_username()