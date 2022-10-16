class parachute:
    def __init__(self) -> None:
        self._parachute_attempt = 4
        self.parachute ={

          
            0:
              """
           
             _____
            /_____\ 
            \     /
             \   /
               0
              /|\ 
              / \
            ^^^^^^^ 
            """,
            1:
            """
            /_____\ 
            \     /
             \   /
               0
              /|\ 
              / \ 
            ^^^^^^^
            """,
            2:
            """
            \     /
             \   /
               0
              /|\ 
              / \ 
            ^^^^^^^
            """,
            3:
            """
             \   /
               0
              /|\ 
              / \ 
            ^^^^^^^
            """,
            4:
            """
               x
              /|\ 
              / \ 
            ^^^^^^^
            """
        }
    def get_parachute(self):
        return self._parachute_attempt
    
    def cut_parachute(self):
         """Decreases the lives count and removes a part of the drawing list.
        
        Args:
            self (Jumper): an instance of Jumper.
"""
         self.parachute -= 1

        
