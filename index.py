import random

class Game:
    def __init__(self):
        self.game_is_on = True
        self.actualPlayer = "X"
        self.winner = None
    def __boards(self):
        board1 = [  "-","-","-",
                    "-","-","-",
                    "-","-","-",    ]
        return(board1)
    def display_board(self):
        print(Game().__boards()[0] + "|" + Game().__boards()[1] + "|" + Game().__boards()[2])
        print(Game().__boards()[3] + "|" + Game().__boards()[4] + "|" + Game().__boards()[5])
        print(Game().__boards()[6] + "|" + Game().__boards()[7] + "|" + Game().__boards()[8])
    


        
Game().display_board()    

