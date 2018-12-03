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
    
    def mark_P1(self, z, x, y):
        self.board[z,x,y] = 1

    def mark_P2(self, z, x, y):
        self.board[z, x, y] = -1

    def is_occpied(self, z, x ,y):
        if self.board[z, x, y] == 1 or self.board[z, x, y] == -1:
            return True
        else:
            return False
    
    '''
    All posible diagonals
    top view left -> right  
    [0, 0, 0] [0, 1, 1] [0, 2, 2] [0, 3, 3]
    [1, 0, 0] [1, 1, 1] [1, 2, 2] [1, 3, 3]
    [2, 0, 0] [2, 1, 1] [2, 2, 2] [2, 3, 3]
    [3, 0, 0] [3, 1, 1] [3, 2, 2] [3, 3, 3]
    top view right -> left
    [0, 0, 3] [0, 1, 2] [0, 2, 1] [0, 3, 0]
    [1, 0, 3] [1, 1, 2] [1, 2, 1] [1, 3, 0]
    [2, 0, 3] [2, 1, 2] [2, 2, 1] [2, 3, 0]
    [3, 0, 3] [3, 1, 2] [3, 2, 1] [3, 3, 0]
    side view left -> right
    [0, 0, 0] [1, 0, 1] [2, 0, 2] [3, 0, 3]
    [0, 1, 0] [1, 1, 1] [2, 1, 2] [3, 1, 3]
    [0, 2, 0] [1, 2, 1] [2, 2, 2] [3, 2, 3]
    [0, 3, 0] [1, 3, 1] [2, 3, 2] [3, 3, 3]
    side view right -> left
    [0, 0, 3] [1, 0, 2] [2, 0, 1] [3, 0, 0]
    [0, 1, 3] [1, 1, 2] [2, 1, 1] [3, 1, 0]
    [0, 2, 3] [1, 2, 2] [2, 2, 1] [3, 2, 0]
    [0, 3, 3] [1, 3, 2] [2, 3, 1] [3, 3, 0]
    front view left -> right
    [0, 0, 3] [1, 1, 3] [2, 2, 3] [3, 3, 3]
    [0, 0, 2] [1, 1, 2] [2, 2, 2] [3, 3, 2]
    [0, 0, 1] [1, 1, 1] [2, 2, 1] [3, 3, 1]
    [0, 0, 0] [1, 1, 0] [2, 2, 0] [3, 3, 0]
    front view right -> left
    [0, 3, 3] [1, 2, 3] [2, 1, 3] [3, 0, 3]
    [0, 3, 2] [1, 2, 2] [2, 1, 2] [3, 0, 2]
    [0, 3, 1] [1, 2, 1] [2, 1, 1] [3, 0, 1]
    [0, 3, 0] [1, 2, 0] [2, 1, 0] [3, 0, 0]
    main diagonals
    [0, 0, 0] [1, 1, 1] [2, 2, 2] [3, 3, 3]
    [3, 0, 3] [2, 1, 2] [1, 2, 1] [0, 3, 0]
    [3, 0, 0] [2, 1, 1] [1, 2, 2] [0, 3, 3]
    [0, 0, 3] [1, 1, 2] [2, 2, 1] [3, 3, 0]
    '''
    def win_condition(self):
        test_elements = [-4, 4]
        #top - > bottom
        for z in range(4):
            for xy in range(4):
                
                
        if (
            np.any(np.isin(np.sum(self.board, axis = 0), test_elements)) or 
            np.any(np.isin(np.sum(self.board, axis = 1), test_elements)) or 
            np.any(np.isin(np.sum(self.board, axis = 2), test_elements))
        ):
            return True
        else:
            return False



class Game:
    game_board = Board()
    player_one = 'P1'
    player_two = 'P2'

    def __init__(self):
        self.game_loop()
    
    def game_loop(self):
        # start game
        # loop start
        while not self.someone_won():
            # ask P1 to make move
            self.player_move(self.player_one)
            # ask P2(AI) to make move
            if self.someone_won():
                print(self.player_one + ' WON!!!')
            else:  
                self.player_move(self.player_two)
                if self.someone_won():
                    print(self.player_two + " WON!!!")
    
    # ask player for coordinates to place his mark
    # check if this spot is avilable
    def ask_for_coordinates(self, player):
        z, x, y = [int(x) for x in input(player + ', where do you want to place yoour marker? : ').split()]
        while(z < 0 or z > 4 or x < 0 or x > 4 or y < 0 or y > 4 or self.game_board.is_occpied(z, x, y)):
            print('Incorrect values or spot is occupied!')
            z, x, y = [int(x) for x in input(player + ', where do you want to place yoour marker? : ').split()]
        return z,x,y

    def player_move(self, player):
        if player == self.player_one:
            z, x, y = self.ask_for_coordinates(player)
            self.game_board.mark_P1(z, x, y)
            self.game_board.print_board()
        else:
            z, x, y = self.game_AI()
            self.game_board.mark_P2(z, x, y)
            self.game_board.print_board()

    def someone_won(self):
        if self.game_board.win_condition():
            return True
        else:
            return False

    def game_AI(self):
        for z in range(4):
            for y in range(4):
                for x in range(4):
                    if not self.game_board.is_occpied(z, x, y):
                        return z, x, y

board = np.zeros((4, 4, 4))
board[0, 0, 0] = 1
board[1, 1, 1] = 1
board[2, 2, 2] = 1
board[3, 3, 3] = 1

print(np.trace(board,axis1=1, axis2=2))

