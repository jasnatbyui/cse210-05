import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
    The hider's location is a random number between 1 and 1000.
    The seeker searches for the hider by guessing its location.
    If the guess is closer to the hider's location it says, "Getting warmer!"
    If the guess is farther away from the hider's location it says, "Getting colder!"
    If the guess is correct the hider says, "You found me!". The game is over.
    """

    def __init__(self, high_num, myName):
        """Constructs a new instance of Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self.high_num = 1000
        self.myName = myName
        self.guessesTaken = 0
        self.number = random.randint(1, self.high_num)
        self.guess = None

class Hider:
       """ The hider's location is a random number between 1 and 1000.
"""

class Game:
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.play():
            self.get_guess()

    def play(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        print('Well, {},  I am thinking of a number between 1 and {}.'
            .format(self.myName, self.high_num))
        while self.guessesTaken < 6:
            if not self.get_guess():
                continue
            # else: self.guess gets changed in get_guess function

            self.guessesTaken += 1
        
            if self.guess < self.number:
                print('Your guess is too low.')
        
            if self.guess > self.number:
                print('Your guess is too high.')
        
            if self.guess == self.number:
                break

        if self.guess == self.number:
            print('Good job, {}! You guessed my number in {} guesses!'
                .format(self.myName, self.guessesTaken))
        else:
            print('Nope. The number I was thinking of was', self.number)
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """

def main():
    print('Hello! What is your name?')
    myName = input()
    print("Right on, {}! We've got 2 brands of game here.".format(myName))

    while True:
        print('Type Y for a guessing game. Type N to quit.')
        user_choice = input()

        if user_choice.lower().startswith('N'):
            print("Goodbye!")
            break

        try:
            user_choice = ("")
            if user_choice not in ["Y","N"]:
                continue
        except ValueError:
            continue

                if user_choice == "Y":
            # make easy game
            easy_game = Game(20, myName)
            # play easy game
            easy_game.play()
            
        elif user_choice == 2:
            # make difficult game
            diff_game = Game(30, myName)
            # play difficult game
            diff_game.play()


        print("\nHow about another?")

class Seeker:
    """A random 
    The responsibility of Guess is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def get_guess(self):
        """Generates a new random value.
        
        Args:
            self (Guess): An instance of Guess.
        """

    def get_guess(self):
        print('Take a guess.')
        try:
            self.guess = int(input())   # the state of this variable is changed of the class instance!
                                        # see more below.
        except ValueError:
            print('Not a valid guess.')
            return False

        return True

    if __name__ == 'main':
     main()

main()
