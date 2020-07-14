import random

board1 = [  "-","-","-",
            "-","-","-",
            "-","-","-"   ]
            
class Game:
    def __init__(self, actualPlayer = "X"):
        self.game_is_on = True
        self.actualPlayer = "X"
        self.winner = None
    def __boards(self, key = None, actualPlayer = "X"):
        if key == None:
            pass
        else:

            if actualPlayer == "0":
  
                if board1[key] == "0":
                    Game().randomSet() 
                if board1[key] == "X":
                    Game().randomSet()
                if board1[key] == "-":
                    board1[key] = actualPlayer
#######################################################
            elif actualPlayer == "X":
                
                if board1[key] == "0":
                    print("Nope. It's alredy taken")
                    Game().actualTurn("X")
                if board1[key] == "X":
                    print("Nope. It's alredy taken")
                    Game().actualTurn("X")
                if board1[key] == "-":
                    board1[key] = actualPlayer


        return(board1) #добавить выбор доски

    def display_board(self):
        print(Game().__boards()[0] + "|" + Game().__boards()[1] + "|" + Game().__boards()[2])  ### но при любом ходе отрисовывает пустую(стартовую доску) 111
        print(Game().__boards()[3] + "|" + Game().__boards()[4] + "|" + Game().__boards()[5])
        print(Game().__boards()[6] + "|" + Game().__boards()[7] + "|" + Game().__boards()[8])
    
    def startGame(self):
        while self.game_is_on:
            Game().actualTurn(self.actualPlayer)
            #Game().changePlayer()
            Game().randomSet()
                            

    def actualTurn(self, actualPlayer):
        Game().display_board()
        actualPlayer = "X"
        key = input("enter pos from 1 to 9: ") #тут добавить isinstanse int
        key = int(key) - 1
        
        if key in range(0,9):
            Game().__boards(key)
        else: 
            print("not in range")


    def randomSet(self):
        actualPlayer = "0"

        key = random.randint(0,9)
        Game().__boards(key, actualPlayer)
        
    
Game().startGame()  

