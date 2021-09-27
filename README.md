# GuessingGame
<br>
The intention of this API is to hold a simple API with which the user, thinking about a number, interacts with, flagging whether the number is above or below, guiding the following guess. In a maximum of 7 attempts, all numbers from 1 to 100 can be guessed by the app. 
<br>
<br>

## Start App
To start the application run:
> python main.py

This will launch the API accessible via <b>localhost:5000</b>
<br>

To reset the game, access the basic end point with:
> {“action”: “start”}

<br>

## Covered interactions
User interactions are managed via the request's body, specifically the action property.
<br>
The available actions are:
- '>' - To flag that the choosen number is greater than the guess.
<br>

- '<' - To flag that the choosen number is 
smaller than the guess.
<br>

- '=' - To flag that the guess was correct.
<br>

- 'start; - To start the guessing game.
