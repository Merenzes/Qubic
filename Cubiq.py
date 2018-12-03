import numpy as np


class Board:
    board = np.array((4, 4, 4))

    def __init__(self):
        self.board = np.zeros((4, 4, 4))

    def print_board(self):
        print(self.board)
        print('_' * 25)

    def mark_P1(self, z, x, y):
        self.board[z, x, y] = 1

    def mark_P2(self, z, x, y):
        self.board[z, x, y] = -1

    def is_occpied(self, z, x, y):
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
        # top view left -> right
        top_one = np.zeros((4, 4))
        for z in range(4):
            for xy in range(4):
                top_one[z, xy] = self.board[z, xy, xy]

        # top view right -> left
        top_two = np.zeros((4, 4))
        for z in range(4):
            for xy in range(4):
                top_two[z, xy] = self.board[z, xy, 3 - xy]

        # side view left -> right
        side_one = np.zeros((4, 4))
        for x in range(4):
            for zy in range(4):
                side_one[x, zy] = self.board[zy, x, zy]

        # side view right -> left
        side_two = np.zeros((4, 4))
        for x in range(4):
            for zy in range(4):
                side_one[x, zy] = self.board[zy, x, 3 - zy]

        # front view left -> right
        front_one = np.zeros((4, 4))
        for y in range(4):
            for zx in range(4):
                front_one[y, zx] = self.board[zx, zx, y]

        # front view right -> left
        front_two = np.zeros((4, 4))
        for y in range(4):
            for zx in range(4):
                front_two[y, zx] = self.board[zx, 3 - zx, y]

        # Main diagonals
        main_diagonals = np.zeros(4)
        main_diagonals[0] = self.board[0, 0, 0] + self.board[1, 1, 1] + self.board[2, 2, 2] + self.board[3, 3, 3]

        main_diagonals[1] = self.board[3, 0, 3] + self.board[2, 1, 2] + self.board[1, 2, 1] + self.board[0, 3, 0]

        main_diagonals[2] = self.board[3, 0, 0] + self.board[2, 1, 1] + self.board[1, 2, 2] + self.board[0, 3, 3]

        main_diagonals[3] = self.board[0, 0, 3] + self.board[1, 1, 2] + self.board[2, 2, 1] + self.board[3, 3, 0]

        if(
            np.any(np.isin(np.sum(self.board, axis=0), test_elements)) or
            np.any(np.isin(np.sum(self.board, axis=1), test_elements)) or
            np.any(np.isin(np.sum(self.board, axis=2), test_elements)) or
            np.any(np.isin(main_diagonals, test_elements)) or
            np.any(np.isin(np.sum(top_two, axis=1), test_elements)) or
            np.any(np.isin(np.sum(top_one, axis=1), test_elements)) or
            np.any(np.isin(np.sum(side_one, axis=1), test_elements)) or
            np.any(np.isin(np.sum(side_two, axis=1), test_elements)) or
            np.any(np.isin(np.sum(front_one, axis=1), test_elements)) or
            np.any(np.isin(np.sum(front_two, axis=1), test_elements))
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
        return z, x, y

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

g = Game()