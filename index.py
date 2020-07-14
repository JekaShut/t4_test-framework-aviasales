import random
import sys

board1 = [  "-","-","-",
            "-","-","-",
            "-","-","-"   ]

board2 = [  "-","-","-","-",
            "-","-","-","-",
            "-","-","-","-",
            "-","-","-","-"   ]

board3 = [  "-","-","-","-","-",
            "-","-","-","-","-",
            "-","-","-","-","-",
            "-","-","-","-","-",
            "-","-","-","-","-"  ]

            
class Game:
    def __init__(self, actualPlayer = "X"):
        self.actualPlayer = "X"
    def __boards(self, key = None, actualPlayer = "X", board = "board1"):
        if key == None:
            pass
        else:
            if actualPlayer == "X":
                
                if board1[key] == "0":
                    print("Nope. It's alredy taken")
                    Game().actualTurn("X")
                if board1[key] == "X":
                    print("Nope. It's alredy taken")
                    Game().actualTurn("X")
                if board1[key] == "-":
                    board1[key] = actualPlayer

            elif actualPlayer == "0":
  
                if board1[key] == "X":
                    Game().randomSet()
                if board1[key] == "0":
                    Game().randomSet() 
                if board1[key] == "-":
                    board1[key] = actualPlayer

        return(board1) 

    def selectBoard(self):
        x = input("Выберите вариант игры: 1 - 3x3, 2 - 4x4, 3 - 5x5 : ")
        board = "board" + x
        Game().startGame(stop=0,board = board)

    def display_board(self):
        print(Game().__boards()[0] + "|" + Game().__boards()[1] + "|" + Game().__boards()[2]) 
        print(Game().__boards()[3] + "|" + Game().__boards()[4] + "|" + Game().__boards()[5])
        print(Game().__boards()[6] + "|" + Game().__boards()[7] + "|" + Game().__boards()[8])
    
    def startGame(self, stop = 0, board = "board1"):
        while stop == 0:
            print(board)
            Game().randomSet()
            Game().check_winner()
            Game().check_end(board = board)
            Game().actualTurn(self.actualPlayer, board = board) 
            Game().check_winner() 
            Game().check_end(board = board) 
        else:
            Game().display_board()
            print("GAME OVER!") 
            sys.exit(0)            

    def actualTurn(self, actualPlayer, board = "board1"):
        Game().display_board()
        actualPlayer = "X"
        error = 1
        while error == 1:
            try:
                key = int(input("enter pos from 1 to 9: "))
                error = 0
            except:
                print("This is not a number. Please enter a number from 1 to 9")
        key = key - 1
        
        if key in range(0,9):
            Game().__boards(key, board = board)
        else: 
            print("not in range")


    def randomSet(self):
        if Game().check_end() == True:
            pass
        else:
            actualPlayer = "0"
            key = random.randint(0,8)
            Game().__boards(key, actualPlayer)
    
    def check_end(self, board = "board1"): 
        if board1.count("-") == 0:
            return(True)
        else: 
            return(False)
    
    def check_winner(self):
        Game().checkWin()

    
    def checkWin(self):
        row_1 = Game().__boards()[0] == Game().__boards()[1] == Game().__boards()[2] != "-"
        row_2 = Game().__boards()[3] == Game().__boards()[4] == Game().__boards()[5] != "-"
        row_3 = Game().__boards()[6] == Game().__boards()[7] == Game().__boards()[8] != "-"

        if row_1 or row_2 or row_3:
            Game().startGame(stop=1)

        column_1 = Game().__boards()[0] == Game().__boards()[3] == Game().__boards()[6] != "-"
        column_2 = Game().__boards()[1] == Game().__boards()[4] == Game().__boards()[7] != "-"
        column_3 = Game().__boards()[2] == Game().__boards()[5] == Game().__boards()[8] != "-"

        if column_1 or column_2 or column_3:
            Game().startGame(stop=1)    

        diagonal_1 = Game().__boards()[0] == Game().__boards()[4] == Game().__boards()[8] != "-"
        diagonal_2 = Game().__boards()[2] == Game().__boards()[4] == Game().__boards()[6] != "-"

        if diagonal_1 or diagonal_2:
            Game().startGame(stop=1)

        

    def checkTie(self):
        pass

        
        
    
Game().selectBoard() 