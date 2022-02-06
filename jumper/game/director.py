from random import random
from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.guess import Guess

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
    The secret word is a random word chosen from a list.
    The player quesses 1 letter from secret word per turn (loop).
    If the guess is correct the letter from the secret word is revealed.
    If the guess is incorrect a line is cut from the player's parachute.
    If the secret word is correctly guessed. The game is over.
    If the player's parachute is gone. The game is over.

    """

    __wordList = ""
    __terminal_service = TerminalService()

    def __init__(self):
        """Constructs a new instance of Director.
        Args:
            self (Jumper): An instance of Director.
        """
        self.__wordList = []
        self.is_playing = True
        self.jumper = Jumper
        self.__terminal_service = TerminalService()

    def start_game(self):
        """Starts the game by running the main game loop. Random word selected.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            word = random.choice(self.wordList)
            return word

    def get_inputs(self):
        """Ask the user if they want to roll.
        Args:
            self (Director): An instance of Director.
        """
        askGuess = self._terminal_service.ask_Guess("Would you like to quess a letter? [y/n] ")
        self.is_playing = (askGuess == "y")

       
    def do_updates(self):
        """Updates the player's guess.
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 




    def do_outputs(self):
        """Displays the result of letter guess ie reveal letter from secret word or remove parachute line. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
