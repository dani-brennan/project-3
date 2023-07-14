<h1>Project 3 - Blackjack<h1>
This app is based on the card game Blackjack, also known as 21’s. The aim of the game is to get a score of 21.

The game lasts 3 rounds, each round the user and dealer(computer) are dealt 2 cards. The user will then be prompted on whether they would like to Hit or Stand. The user's goal is to get a higher score than the dealer, but the card value total must not exceed 21. If the user’s/computer's total card value goes over 21, they bust and they have lost. 

[final screenshots]

<a href="https://db-project3-c5b4318d6ba5.herokuapp.com/">Link to deployed project</a>
<h2>Technologies Used</h2>
Python

<h2>User stories </h2>
<h3>Current User Goals</h3>
To allow the user to enjoy multiple rounds of Blackjack. Every round is randomised which makes it different for the user on each playthrough.
<h3>New User Goals</h3>
To learn how to play Blackjack.
<h2>Future Goals</h2>
In the future I would like to implement a betting system where the user can choose the amount they would like to bet before each round.

<h2>Features</h2>
This app will begin with displaying the game title and a welcome message and ask the user for their name. The user will also be asked if they would like to learn how to play. The choices will be either yes(Y) or no(N).
<h3>How to play</h3>
The aim of this game is to get a score of 21 or a higher score than the computer, as long as it does not go over 21. During each round the player will be given the choice to hit or stand. They can keep hitting until they are bust. If the player gets a blackjack it will result in a win, if the computer gets a blackjack it will result in a loss. If the player and computer obtain the same score, it will result in a tie.

Error Handling
If the user does not enter a correct prompt from the selection given, such as Y or N, it will prompt the user again to put in the correct information.

<h2>Testing</h2>
Validator Testing
This code was tested by using CI PEP8 Online. 

<h3>Errors Found</h3>


<h3>After testing</h3>



<h2>Manual Testing</h2>



<h3>Unfixed Bugs</h3>
None that I am aware of.

<h2>Frameworks, Libraries & Programs</h2>
Gitpod
GitHub
Heroku 
Random - to randomize the cards for every round of Blackjack.

<h2>Deployment<h2>
This app was deployed to Heroku. 
After creating an account and logging in, create a new app.
Choose a name and click Create App.
In "Settings" find Config Vars and add KEY = PORT : VALUE = 8000.
Find the Deploy tab and select GitHub under the deployment method.
Select your repository you want deployed and connected to Heroku.
Click deploy

<h2>Credits</h2>
To learn how to create a basic blackjack game I followed the tutorial by
https://www.youtube.com/watch?v=aryte85bt_M. It helped me to understand the logic and really helped me improve my knowledge of Python. 
I learned how to deploy this project to Heroku by following Code Institute's love_sandwiches walkthrough.
