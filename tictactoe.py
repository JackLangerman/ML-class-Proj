class Board:
    
    def __init__(self, p1, p2):
#         self.state = [['0', '1', '2'],
#                       ['3', '4', '5'],
#                       ['6', '7', '8']]
        self.state = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

        self.p1 = p1
        self.p2 = p2
        
    def __str__(self):
        return ("\n".join([" ".join(line) for line in self.state]))

#     def getMove(player):
#         move, token = player.getMove(self.state)
    def isLegal(self, move):
        print(type(move[0]), move[1])
        return (move[0] >= 0 and move[0] < 3 
                and move[1] >= 0 and move[1] < 3 
                and self.state[move[0]][move[1]] == '-')
            
    def apply(self, move, token):
        print(token)
        self.state[move[0]][move[1]] = token
        
    def gameOver(self):
        return False


#--------
b = Board(1, 2)
#--------
print(b.p1)
print(b.p2,"\n")
# print(b.state)
print(b)
#-------
class TicTacToe:
    def __init__(self, p1, p2):
        self.board = Board(p1,p2)
        self.p1 = p1
        self.p2 = p2
    
    def play(self):
        cur = self.p1
        while True:
            move = cur.getMove(self.board.state)
            if self.board.isLegal(move):
                print("change")
                token = 'X' if cur==p1 else 'O'
                print(token, cur, p1, p2)
                self.board.apply(move, token)
                cur = self.p2 if cur==self.p1 else self.p2
            else:
                print("illegal")
                
            if self.board.gameOver():
                print("And the winner is...\n...{}")
                print(cur)
                break
            
#---------------
class Player:
    def getMove(board):
        print("The board state is as follows:")
        print(board)
        print("\nWhat is your move (row col)?".format(board))
        raw = input()
        spltRaw = raw.split(" ")
        move = (int(spltRaw[0]), int(spltRaw[1]))
        print(move)
        return move
#-------------
p1, p2 = Player, Player
ttt = TicTacToe(p1, p2)
#-------------
ttt.play()

