## Overview
Seeker is a game in which the player seeks to find the hider by guessing its location. The hider gives hints until it is found.

## Rules
Seeker is played according to the following rules.

The hider's location is a random number between 1 and 1000.
The seeker searches for the hider by guessing its location.
If the guess is closer to the hider's location it says, "Getting warmer!"
If the guess is farther away from the hider's location it says, "Getting colder!"
If the guess is correct the hider says, "You found me!". The game is over.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
python3 dice 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- seeker                (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Jason McLaughlin (jasnatbyui@gmail.com)
