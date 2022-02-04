import random


class Guess:
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
        print('Take a guess.')
        try:
            self.guess = int(input())
        except ValueError:
            print('Not a valid guess.')
            return False
            
        return True
