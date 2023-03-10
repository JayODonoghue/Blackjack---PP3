# BLACKJACK

<br/>

This is your typical game of Blackjack using python backend programming to complete. The user story is to create a single player game. The aim is for natural flowing game returning a good user experience. Inputs are used throughout provide constant interaction with the user along with cues for any ease of use. The user (you) begins the game with 1000 coins. You then place your wager and draw card. The dealer (computer) gets dealt two cards also however one is hidden. You are then presented with the option to 'hit' or 'stand'. If hit is chosen the user draws another card and if not bust is goven the option  of 'hit' or 'stand' again. If stand is chosen then the dealers cards are shown. If the dealer is under 17 then they have to automatically hit. If they are between 17 and 21 then the dealer and user scores are compared. If either player goes bust, the other wins. The aim is to get as close to 21 as possible. If you reach 21 Blackjack is declared. Otherwise the player with the highest total is the winner. If it is a draw its called a push. Once a winner/loser/draw is determined our winngs/losses will be adjusted accordingly.

 <br/> 

![Blackjack Game](readme-doc/images/amiresponsive-blackjack-image.png)

[View Blackjack live game on Github pages here](https://blackjack-pp3.herokuapp.com/)

---

## CONTENT

* [FLow Chart](#flow-chart)

<br/>

* [Features](#features)
  * [Start up](#start-up)
  * [Instructions choice](#instructions-choice)
  * [Instructions](#instructions)
  * [Place bet](#place-bet)
  * [Cards are dealt and hit or stand option given](#cards-are-dealt-and-hit-or-stand-option-given)
  * [Check dealer card and winnning hand](#check-dealer-card-and-winnning-hand)
  * [Go again](#go-again)
  * [Python modules used](#python-modeules-used)

<br/>

  * [Future Implementations](#future-implementations)

<br/>

* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

<br/>

* [Testing](#testing)
    * [CI Python Linter](#CI-Python-Linter)
    * [Manual Testing](#manual-testing)
    * [Solved Bugs](#solved-bugs)
    * [Known Bugs](#known-bugs)
   
<br/>

* [Deployment](#deployment)

<br/>

* [Credits](#credits)
  * [Layout](#layout)
  * [Content](#content)
  * [Code](#code)
  * [Acknowledgements](#acknowledgements)

---

<br/>

## FLOW CHART

This flow chart was used to design the game.

![Blackjack Flow Chart](readme-doc/images/blackjack-flowchart.png)

<br/>

## Features

<br/>

### Start up

![Blackjack Start up](readme-doc/images/blackjack_home_screen_image.png)

The game begins with the word Blackjack in red ASCII text. It then tells you to input your username. This input will need to be between 3 and 10 characters. If invalid data is given, a message is returned using a while loop reiterating the conditions for it to be successful.

<br/>

### Instructions choice

![Instructions choice](readme-doc/images/instructions-choice-image.png)

The user is given the option to start the game or read the instruction. Invalid data will not be accepted. This again is done through a while loop. If s is entered then move on, if i chosen then the user is brought to the instructions page.

<br/>

### Instructions

![Instructions](readme-doc/images/instructions-image.png)

The user is shown the way the game works and then given the choice of playing the game or returing to the start up scrren, again using an input for the response.

<br/>

### Place bet

![Place bet](readme-doc/images/place-bet-image.png)

The user is asked to input a wager that has to be a minimum of 10 and and a multiple of 5. A Value Error is returned if not inputted correctly. The users coins are shown at the top left hand corner of the screen. This figure increase and decreases depending on whether you win or lose.

<br/>

### Cards are dealt and hit or stand option given

![Cards are dealt and hit or stay input](readme-doc/images/hit-or-stay-image.png)

The cards are dealt using the random module.  One of the dealer's cards is hidden. An option is presented to the user, to hit or stand. If h is entered then an additional card is dealt and the users total is adjusted to accomodate the new card. If stand it moves on to check the dealers hand.

<br/>

### Check dealer card and winnning hand

![Check dealers hand and compare hands](readme-doc/images/dealer-cards-and-winning-hand-image.png)

If user is not gone bust then the dealers hand is revealed. If the dealer is between 17 and 21 it automatically stands and the total scores are compared in winng hand function. If the dealer's total is under 17 then they draw an additional card until they either go bust or go higher than 17, this is done using a while loop. The winning hand function compares the 2 totals and declares a winner based on if/elif statements.

<br/>

### Go again

![Go again, print goodbye when finished](readme-doc/images/go-again-goodbye-image.png)

If the user runs out of coins then the game resets and goes back to the start up screen. GOODBYE is printed for a brief time using the time module and using ASCII text. If the user still has coins left then he is giving the option to play again or to quit. If play again is entered the main function is called and a new is started. If q is chosen the user returns to the start up screen.

<br/>

### Python modules used:
  * import os - used to clear system once implemented in the clear function.
  * import random - used to randomly choose a card for the deck.
  * import time - used time.sleep to display text for brief periods.
  * import pyfiglet - used to add ASCII text 
  * import termcolor -  used to add color to text

  <br/>

## Future Implementations:
  * Use ASCII to actually display cards rather than stating them in standard text.
  * Use a class for card which would reduce a lot of lines of code resulting in it being more efficient.
  * When dealing is displayed on the screen an audio sound of cards being shuffled would be a nice additional feature.
  * Create a virtual casino by adding more game options to choose from.

  <br/>

## Technologies Used

<br/>

### Languages Used

<br/>

* Python

<br/>

### Frameworks and Programs Used

* Git - This was used for version control.
* Github - This was used to save and store all the files for the website.
* Am I Responsive - This was used to show the website on a variety of different screens.
* Code Institute template was used to create this project on Gitpod.
* Heroku was used for deployment.

<br/>

## Testing

<br/>

### CI Python Linter

The CI Python Linter was used on every aspect of Python in the project. No errors were returned.

![CI Python Linter Report](readme-doc/images/ci-python-linter-image.png)

<br/>

### Manual Testing

* I have gone through every input making sure invalid inputs will not be accepted. Invalid inputs: strings when numbers required, out of bound inputs, below minimum  and maximum requirements inputs and in the place bet function an input that is not a multiple of 5 or exceeds the total coins of the user.
* Tested in my local terminal and the Code Institute Heroku terminal.

<br/>  

### Solved Bugs

<br/>

1. When implementing the player_coins variable in the main() function the wager amount was not being added or subtracted after every round. However once I removed it from the main function and start_up function and put it in the global scope it was resolved.

2. When an ace card was dealt the code I had written for aces was not working correctly distinguishing between 1 and 11. After doing some research I found a way to count the aces, so if an 'A' is drawn the ace count goes up one. If the value is over 21 then the total minuses 10 and the ace count subtracts 1.

3. In the check_dealer_hand, when the user went bust it was reporting an error. Throught the help of my mentor we realised it was a simple fix of g=the go_again() function required to be called up as it was leading to nothing otherwise.

<br/>

### Known Bugs

<br/>

In the run.py file no line length exceeds 80. However in the terminal some words in the instructions carry on to the next line which is not aesthetically pleasing. This can be solved with shorter sentences and more line breaks.

<br/>

## Deployment:
This game was deployed on Heroku. The following steps were used to deploy the game to Heroku.
- First make sure you are signed into Heroku.
- Then on the main dashboard select **New** and then choose **Create new app** from the drop down menu.
- Then you will need to choose a name for your project(this name has to be unique to Heroku) and also choose the region, based on where you are located(as I'm in Europe, I chose Europe)
and then click on **Create app**.
- Then go to the **Settings** tab.
- In **Settings** click on **Reveal Config Vars** and enter the following key **Port** with the Value of **8000**.
- If you are using a Google sheets API in your project you will need to enter **Creds** as another **Config Var**.
- Next scroll down to **Buildpacks** and click **Add buildpack** choose **Python** and then click **Save changes**.
- Repeat the above step and select **nodejs** and click **Save changes**.
- Next go to the **Deploy tab**.
- Under **Deployment method** choose Github and then click **Connect to GitHub** you will probably be prompted to sign into your Github.
- Then you can search for your GitHub repository, in my case this was **blackjack** and click **connect**.
- To deploy automatically you will need to select **Enable Automatic Deploys** which will rebuild the app everytime you push a change to GitHub.
- To deploy manually go to the **Manual deploy** section below and click **Deploy Branch**. Just remember you will need to do this everytime you make a change to your
code on Github.
- Below you will see **your app was sucessfully deployed** with a **view** button below this that will take you to the url of your deployed app.

<br/>

## Credits

### Layout
* The layout of the site was established by me. 
* The layout of this readme file is based off my previous projects readme.

<br/>

### Content 
* The content was written by Jay O'Donoghue.

<br/>

### Code
* I watched a tutorial by [Learn Learn Scratch Tutorials](https://www.youtube.com/watch?v=U1aUteSg2a4) which showed me how to use ASCII text.
* I used code from [Gayan Samarakoon](https://samarakoon-gayan.medium.com/a-game-of-black-jack-on-python-as-a-fun-exercise-3cd54efb9d83) to create the class for the coins and to adjust for the aces.
* I visited the website [Scaler](https://www.scaler.com/topics/how-to-clear-screen-in-python/) to figure out how to clear screen module.
* Stack overflow helped in showing me how to use pyfiglet, time and random modules.
* For the deployment section of this readme file I have used the same process as previous students. 

<br/>

### Acknowledgements
* I would like to thank my mentor Chris in guiding me in the right direction and helping whenever I had a query.
* I would like to thank the people who reviewed my code in peer-code-review on Slack.
* I would like to thank the tutor support people who answered all the queries I had throughout the project.
* I would like to thank the cohort lead and the cohort Facilitator on checking up and keeping everyone on schedule.
