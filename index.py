import random

class Game:
    def __init__(self):
        self.game_is_on = True
        self.actualPlayer = "X"
        self.winner = None
    def __boards(self, key = None):


        board1 = [  "-","-","-",
                    "-","-","-",
                    "-","-","-"   ]
        if key == None:
            pass
        else:
            board1[key] = "x"

        return(board1) #добавить выбор доски
    def display_board(self):
        print(Game().__boards()[0] + "|" + Game().__boards()[1] + "|" + Game().__boards()[2])
        print(Game().__boards()[3] + "|" + Game().__boards()[4] + "|" + Game().__boards()[5])
        print(Game().__boards()[6] + "|" + Game().__boards()[7] + "|" + Game().__boards()[8])
    
    def startGame(self):
        while self.game_is_on:
            Game().changeTurn(self.actualPlayer)

    def changeTurn(self, actualPlayer):
        key = input("enter pos from 1 to 9: ") #тут добавить isinstanse int
        key = int(key) - 1
        Game().__boards(key)
        Game().display_board()
        
    def changePlayer(self):
        pass


        
Game().startGame()  

