
class Director():


    def __init__(self):
      self.score = 300

    def win(self):
      self.score += 100
      

    def lose(self):
      self.card -= 75
      if self.score < 0:
            self.score = 0

    def get_score(self):
      return (self.score)
