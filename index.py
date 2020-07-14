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
            
            print(Game().__boards()[0] + "|" + Game().__boards()[1] + "|" + Game().__boards()[2] + "     1 | 2 | 3")
            print(Game().__boards()[3] + "|" + Game().__boards()[4] + "|" + Game().__boards()[5] + "     4 | 5 | 6")
            print(Game().__boards()[6] + "|" + Game().__boards()[7] + "|" + Game().__boards()[8] + "     7 | 8 | 9")
        if num == 1:
            print(Game().__boards(num=num)[0] + "|" + Game().__boards(num=num)[1] + "|" + Game().__boards(num=num)[2] + "|" + Game().__boards(num=num)[3] + "     1  | 2  | 3  | 4")
            print(Game().__boards(num=num)[4] + "|" + Game().__boards(num=num)[5] + "|" + Game().__boards(num=num)[6] + "|" + Game().__boards(num=num)[7] + "     5  | 6  | 7  | 8")
            print(Game().__boards(num=num)[8] + "|" + Game().__boards(num=num)[9] + "|" + Game().__boards(num=num)[10] + "|" + Game().__boards(num=num)[11] + "     9  | 10 | 11 | 12")
            print(Game().__boards(num=num)[12] + "|" + Game().__boards(num=num)[13] + "|" + Game().__boards(num=num)[14] + "|" + Game().__boards(num=num)[15] + "     13 | 14 | 15 | 16")
        if num == 2:
            print(Game().__boards(num=num)[0] + "|" + Game().__boards(num=num)[1] + "|" + Game().__boards(num=num)[2] + "|" + Game().__boards(num=num)[3] + "|" + Game().__boards(num=num)[4] + "     1  | 2  | 3  | 4  | 5")
            print(Game().__boards(num=num)[5] + "|" + Game().__boards(num=num)[6] + "|" + Game().__boards(num=num)[7] + "|" + Game().__boards(num=num)[8] + "|" + Game().__boards(num=num)[9] + "     6  | 7  | 8  | 9  | 10")
            print(Game().__boards(num=num)[10] + "|" + Game().__boards(num=num)[11] + "|" + Game().__boards(num=num)[12] + "|" + Game().__boards(num=num)[13] + "|" + Game().__boards(num=num)[14] + "     11 | 12 | 13 | 14 | 15")
            print(Game().__boards(num=num)[15] + "|" + Game().__boards(num=num)[16] + "|" + Game().__boards(num=num)[17] + "|" + Game().__boards(num=num)[18] + "|" + Game().__boards(num=num)[19] + "     16 | 17 | 18 | 19 | 20")
            print(Game().__boards(num=num)[20] + "|" + Game().__boards(num=num)[21] + "|" + Game().__boards(num=num)[22] + "|" + Game().__boards(num=num)[23] + "|" + Game().__boards(num=num)[24] + "     21 | 22 | 23 | 24 | 25")

    def startGame(self, stop = 0, num=0, board = [board1, board2, board3]):
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
        if num == 0: #3x3
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
        
        if num == 1: #4x4
            row_1 = Game().__boards(num = num)[0] == Game().__boards(num = num)[1] == Game().__boards(num = num)[2] == Game().__boards(num = num)[3] != "-"
            row_2 = Game().__boards(num = num)[4] == Game().__boards(num = num)[5] == Game().__boards(num = num)[6] == Game().__boards(num = num)[7] != "-"
            row_3 = Game().__boards(num = num)[8] == Game().__boards(num = num)[9] == Game().__boards(num = num)[10] == Game().__boards(num = num)[11] != "-"
            row_4 = Game().__boards(num = num)[12] == Game().__boards(num = num)[13] == Game().__boards(num = num)[14] == Game().__boards(num = num)[15] != "-"

            if row_1 or row_2 or row_3 or row_4:
                Game().startGame(stop=1, num = num)  

            column_1 = Game().__boards(num = num)[0] == Game().__boards(num = num)[4] == Game().__boards(num = num)[8] == Game().__boards(num = num)[12] != "-"
            column_2 = Game().__boards(num = num)[1] == Game().__boards(num = num)[5] == Game().__boards(num = num)[9] == Game().__boards(num = num)[13] != "-"
            column_3 = Game().__boards(num = num)[2] == Game().__boards(num = num)[6] == Game().__boards(num = num)[10] == Game().__boards(num = num)[14] != "-"
            column_4 = Game().__boards(num = num)[3] == Game().__boards(num = num)[7] == Game().__boards(num = num)[11] == Game().__boards(num = num)[15] != "-"
            
            if column_1 or column_2 or column_3 or column_4:
                Game().startGame(stop=1, num = num) 

            diagonal_1 = Game().__boards(num = num)[0] == Game().__boards(num = num)[5] == Game().__boards(num = num)[10] == Game().__boards(num = num)[15] != "-"
            diagonal_2 = Game().__boards(num = num)[3] == Game().__boards(num = num)[6] == Game().__boards(num = num)[9] == Game().__boards(num = num)[12] != "-"

            if diagonal_1 or diagonal_2:
                Game().startGame(stop=1, num = num)

        if num == 2: #5x5
            row_1 = Game().__boards(num = num)[0] == Game().__boards(num = num)[1] == Game().__boards(num = num)[2] == Game().__boards(num = num)[3] == Game().__boards(num = num)[4] != "-"
            row_2 = Game().__boards(num = num)[5] == Game().__boards(num = num)[6] == Game().__boards(num = num)[7] == Game().__boards(num = num)[8] == Game().__boards(num = num)[9] != "-"
            row_3 = Game().__boards(num = num)[10] == Game().__boards(num = num)[11] == Game().__boards(num = num)[12] == Game().__boards(num = num)[13] == Game().__boards(num = num)[14] != "-"
            row_4 = Game().__boards(num = num)[15] == Game().__boards(num = num)[16] == Game().__boards(num = num)[17] == Game().__boards(num = num)[18] == Game().__boards(num = num)[19] != "-"
            row_5 = Game().__boards(num = num)[20] == Game().__boards(num = num)[21] == Game().__boards(num = num)[22] == Game().__boards(num = num)[23] == Game().__boards(num = num)[24] != "-"

            if row_1 or row_2 or row_3 or row_4 or row_5:
                Game().startGame(stop=1, num = num) 

            column_1 = Game().__boards(num = num)[0] == Game().__boards(num = num)[5] == Game().__boards(num = num)[10] == Game().__boards(num = num)[15] == Game().__boards(num = num)[20] != "-"
            column_2 = Game().__boards(num = num)[1] == Game().__boards(num = num)[6] == Game().__boards(num = num)[11] == Game().__boards(num = num)[16] == Game().__boards(num = num)[21] != "-"
            column_3 = Game().__boards(num = num)[2] == Game().__boards(num = num)[7] == Game().__boards(num = num)[12] == Game().__boards(num = num)[17] == Game().__boards(num = num)[22] != "-"
            column_4 = Game().__boards(num = num)[3] == Game().__boards(num = num)[8] == Game().__boards(num = num)[13] == Game().__boards(num = num)[18] == Game().__boards(num = num)[23] != "-"
            column_5 = Game().__boards(num = num)[4] == Game().__boards(num = num)[9] == Game().__boards(num = num)[14] == Game().__boards(num = num)[19] == Game().__boards(num = num)[24] != "-"
            
            if column_1 or column_2 or column_3 or column_4 or column_5:
                Game().startGame(stop=1, num = num) 

            diagonal_1 = Game().__boards(num = num)[1] == Game().__boards(num = num)[6] == Game().__boards(num = num)[12] == Game().__boards(num = num)[18] == Game().__boards(num = num)[24] != "-"
            diagonal_2 = Game().__boards(num = num)[4] == Game().__boards(num = num)[8] == Game().__boards(num = num)[12] == Game().__boards(num = num)[16] == Game().__boards(num = num)[20] != "-"

            if diagonal_1 or diagonal_2:
                Game().startGame(stop=1, num = num)
            

Game().selectBoard() 