import random
import sys
from os import system

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
    def __boards(self, key = None, actualPlayer = "X", board = [board1, board2, board3], num = 0):
        
        if key == None:
            pass
        else:
            if actualPlayer == "X":
                
                if board[num][key] == "0":
                    print("Nope. It's alredy taken")
                    Game().actualTurn("X", num=num)
                if board[num][key] == "X":
                    print("Nope. It's alredy taken")
                    Game().actualTurn("X", num=num)
                if board[num][key] == "-":
                    board[num][key] = actualPlayer

            elif actualPlayer == "0":
  
                if board[num][key] == "X":
                    Game().randomSet()
                if board[num][key] == "0":
                    Game().randomSet() 
                if board[num][key] == "-":
                    board[num][key] = actualPlayer

        return(board[num]) 

    def selectBoard(self):
        x = input("Выберите вариант игры: 1 - 3x3, 2 - 4x4, 3 - 5x5 : ")
        num = int(x)-1
        board = [board1, board2, board3]
        Game().startGame(stop=0,board=board, num=num)

    def display_board(self,num = 1):
        
        if num == 0:
            
            print(Game().__boards()[0] + "|" + Game().__boards()[1] + "|" + Game().__boards()[2]) 
            print(Game().__boards()[3] + "|" + Game().__boards()[4] + "|" + Game().__boards()[5])
            print(Game().__boards()[6] + "|" + Game().__boards()[7] + "|" + Game().__boards()[8])
        if num == 1:
            print(Game().__boards(num=num)[0] + "|" + Game().__boards(num=num)[1] + "|" + Game().__boards(num=num)[2] + "|" + Game().__boards(num=num)[3])
            print(Game().__boards(num=num)[4] + "|" + Game().__boards(num=num)[5] + "|" + Game().__boards(num=num)[6] + "|" + Game().__boards(num=num)[7])
            print(Game().__boards(num=num)[8] + "|" + Game().__boards(num=num)[9] + "|" + Game().__boards(num=num)[10] + "|" + Game().__boards(num=num)[11])
            print(Game().__boards(num=num)[12] + "|" + Game().__boards(num=num)[13] + "|" + Game().__boards(num=num)[14] + "|" + Game().__boards(num=num)[15])
        if num == 2:
            print(Game().__boards(num=num)[0] + "|" + Game().__boards(num=num)[1] + "|" + Game().__boards(num=num)[2] + "|" + Game().__boards(num=num)[3] + "|" + Game().__boards(num=num)[4])
            print(Game().__boards(num=num)[5] + "|" + Game().__boards(num=num)[6] + "|" + Game().__boards(num=num)[7] + "|" + Game().__boards(num=num)[8] + "|" + Game().__boards(num=num)[9])
            print(Game().__boards(num=num)[10] + "|" + Game().__boards(num=num)[11] + "|" + Game().__boards(num=num)[12] + "|" + Game().__boards(num=num)[13] + "|" + Game().__boards(num=num)[14])
            print(Game().__boards(num=num)[15] + "|" + Game().__boards(num=num)[16] + "|" + Game().__boards(num=num)[17] + "|" + Game().__boards(num=num)[18] + "|" + Game().__boards(num=num)[19])
            print(Game().__boards(num=num)[20] + "|" + Game().__boards(num=num)[21] + "|" + Game().__boards(num=num)[22] + "|" + Game().__boards(num=num)[23] + "|" + Game().__boards(num=num)[24])

    def startGame(self, stop = 0, num=0, board = [board1, board2, board3]):
        print(str(num) + "startGame")
        num = num
        while stop == 0:
            
            Game().randomSet(num = num)
            Game().check_winner(num = num)
            Game().check_end(board = board, num = num)
            Game().actualTurn(self.actualPlayer, board = board, num=num) 
            Game().check_winner(num = num) 
            Game().check_end(board = board, num = num) 
        else:
            Game().display_board(num = num)
            print("GAME OVER!") 
            sys.exit(0)            

    def actualTurn(self, actualPlayer, board = [board1, board2, board3], num = 0):
        
        Game().display_board(num = num)
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
            Game().__boards(key, board = board, num=num)
        else: 
            print("not in range")


    def randomSet(self, num=0):
        if Game().check_end(num = num) == True:
            pass
        else:
            actualPlayer = "0"
            key = random.randint(0,8)
            Game().__boards(key, actualPlayer, num=num)
    
    def check_end(self, board = [board1, board2, board3], num = 0): 
        
        if board[num].count("-") == 0:
            return(True)
        else: 
            return(False)
    
    def check_winner(self, num = 0):
        Game().checkWin(num = num)

    
    def checkWin(self, num = 0):
        row_1 = Game().__boards()[0] == Game().__boards()[1] == Game().__boards()[2] != "-"
        row_2 = Game().__boards()[3] == Game().__boards()[4] == Game().__boards()[5] != "-"
        row_3 = Game().__boards()[6] == Game().__boards()[7] == Game().__boards()[8] != "-"

        if row_1 or row_2 or row_3:
            Game().startGame(stop=1, num = num)

        column_1 = Game().__boards()[0] == Game().__boards()[3] == Game().__boards()[6] != "-"
        column_2 = Game().__boards()[1] == Game().__boards()[4] == Game().__boards()[7] != "-"
        column_3 = Game().__boards()[2] == Game().__boards()[5] == Game().__boards()[8] != "-"

        if column_1 or column_2 or column_3:
            Game().startGame(stop=1, num = num)    

        diagonal_1 = Game().__boards()[0] == Game().__boards()[4] == Game().__boards()[8] != "-"
        diagonal_2 = Game().__boards()[2] == Game().__boards()[4] == Game().__boards()[6] != "-"

        if diagonal_1 or diagonal_2:
            Game().startGame(stop=1, num = num)

        

    def checkTie(self):
        pass

        
        
    
Game().selectBoard() 