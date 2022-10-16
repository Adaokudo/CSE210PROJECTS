from gam.terminal_service import TerminalService
from gam.board import parachute
from gam.word import word


class Director:
   """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        board:
        is_playing (boolean): Whether or not the game is being played.
        word: 
        terminal services (int):
"""

   def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """

        self.board = parachute()
        self.word = word()
        self.is_playing = True
        
   def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

   def _get_inputs(self):
        """"gets a letter from the player to match the word. .


        Args:
            self (Director): An instance of Director.
        """
        current_guess = self._terminal_service.read_number("You already guessed that. Please guess a new letter [a-z]: ")
       
        
   def _do_updates(self):
        """updates the new words from the guesser.

        Args:
            self (Director): An instance of Director.
        """
        self(self)
        
   def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
      
        self._terminal_service.write()
        if self._is_win():
            self._is_playing = False



