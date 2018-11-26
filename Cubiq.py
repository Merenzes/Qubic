import numpy as np

class Board:
    board = np.array((4,4,4))

    def __init__(self):
        self.board = np.zeros((4,4,4))
        #self.board.fill("-")
    
    def print_board(self):
        print(self.board)
        #print('top \n', self.board[0], '\n mid \n', self.board[1], '\n bottom \n', self.board[2])
        print('_'* 25)
    
    def mark_cross(self, z, x, y):
        self.board[z,x,y] = 1

    def mark_os(self, z, x, y):
        self.board[z, x, y] = 2

class Game:
    game_board = Board()
    player_one = 'P1'
    player_two = 'P2'

    #def __init__(self):
        
    
    #def game_loop():
        #satrt game
        #ask P1 to make move
        #check for win
        #ask P2 to make move
        #check for win
        #repeat above until one player win or there are no chance to win
'''
    def check_win(self):
        win = False
        where = [0,0,0]
        #columns between planes
        if (self.game_board[0,0,0] == self.gmae_board[1,0,0] and 
            self.game_board[0,0,0] == self.gmae_board[2,0,0] and
            self.game_board[0,0,0] == self.gmae_board[3,0,0]):
                win = True
                where = [0,0,0]
        
        
        return win, where
'''


#b = Board()
#b.print_board()
#b.mark_cross(0,1,2)
#b.print_board()


board = np.arange(64).reshape(4,4,4)
print(board)
#print("up plane first column")
#print(board[0,:,0])
#print("[0,0] from 2 planes")
#print(board[:,0,0])
#s = np.all(board == board[:,0,0])
#print(s)
