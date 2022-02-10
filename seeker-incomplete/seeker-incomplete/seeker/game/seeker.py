
class Seeker:
    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """


    """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
    def __init__(self):
        self._location = 0
       
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
    def get_location(self):
        number = self._location
        return number        

        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
    def move_location(self, location):
        self._location = location

