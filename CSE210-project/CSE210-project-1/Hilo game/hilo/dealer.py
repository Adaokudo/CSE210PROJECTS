from card import Card

class Dealer:
    


    def __init__(self):
        self.card = ()
        self.is_playing = True
        self.card_value = 0
        self.total_score = 0 
        self.get_input= "" 
        play_again = 'y'
       

    def get_input(self):
        """ get-input ask player for their guess
        and the players guess is returned
        
        """   
        self.user_input = input("guess if the next number will be higher or lower ")
        return (self.get_input)  
        
    def do_updates(self):
        """do_update check if the player is correct.
        If the player guessed correctly, the player's score is incremented.
        If the player guessed incoreectly, the player's score is decremented.
        """      

        if self.user_input > self.get_card_value:
                print("you guessed right!")
                self.director = self.win
                return
        if self.user_input < self.get_card_value:
                print("you guessed right!")
                self.director = self.win
                return
        else:         
             self.director = self.lose
    
    def start_game(self):
       
        while play_again:  
         print("Welcome to HiLo! You start your game with 300 points.")      
         self.card_value = self.card.get_face_value()
         print('the card is:'.format(self.card_value))

         self.get_inputs = self.get_inputs()
         self.card1_value = self.card.get_face_value()
        
         print("The card is {}".format(self.card_value))

          
         self.user_input = self.get_input()

         self.user_input = self.do_updates()
         print("Your score is: ", self.director.get_score())

         

        if (self.director.get_score() > 0):
            print("Good game! your score is {}".format(self.director.get_score()))   
        else: 
            print("You have lost all your points and the game is over.")
                
           
                
        