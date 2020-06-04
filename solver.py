import math
import time

class Board:
    
    RED = '\033[91m'
    ENDC = '\033[0m'
    size = 9

    def __init__(self, grid):
        self.grid = grid
    
    def check_across(self, possible_options, row):
        for col in range(Board.size):
            if self.grid[row][col] in possible_options: possible_options.remove(self.grid[row][col])
        return possible_options
    
    def check_down(self, possible_options, col):
        for row in range(Board.size):
            if self.grid[row][col] in possible_options: possible_options.remove(self.grid[row][col])
        return possible_options
    
    def check_square(self, possible_options, row, col):
        small_size = int(math.sqrt(Board.size))
        corner_row = int(row / small_size) * small_size
        corner_col = int(col / small_size) * small_size 
        for row in range(small_size):
            for col in range(small_size):
                if self.grid[corner_row + row][corner_col + col]in possible_options: possible_options.remove(self.grid[corner_row + row][corner_col + col])
        return possible_options

    def get_options(self, row, col):
        possible_options = {1,2,3,4,5,6,7,8,9}
        possible_options = self.check_across(possible_options, row)
        possible_options = self.check_down(possible_options, col)
        possible_options = self.check_square(possible_options, row, col)
        return possible_options

    def solve(self):
        run_count = 0
        done = False
        while not done:
            count = 0
            for row in range(Board.size):
                for col in range(Board.size):
                    if not self.grid[row][col] == 0:
                        count += 1
                    else:
                        possible_options = self.get_options(row, col)
                        if len(possible_options) == 1:
                            self.grid[row][col] = possible_options.pop()
                            count += 1
                    done = count == self.size**2
            run_count += 1
            print('Run {}...{}'.format(run_count, count))
            time.sleep(0.5)
        self.show()

    def show(self):
        for row in range (9):
            if row % 3 == 0:
                print('-------------------')
            for col in range (9):
                if col % 3 == 0:
                    print('|', end='')
                print(Board.RED + str(self.grid[row][col]) + Board.ENDC, end = '') 
                if col % 3 != 2:
                    print(' ', end = '')
            print('|')
        print('-------------------')



g0 = [0, 0, 8, 0, 0, 0, 7, 0, 0] 
g1 = [3, 0, 0, 0, 2, 5, 0, 0, 0]
g2 = [9, 0, 2, 0, 0, 0, 0, 3, 5]
g3 = [0, 0, 0, 2, 0, 9, 0, 0, 8]
g4 = [0, 2, 0, 6, 0, 8, 0, 9, 0]
g5 = [4, 0, 0, 5, 0, 3, 0, 0, 0]
g6 = [8, 4, 0, 0, 0, 0, 2, 0, 3]
g7 = [0, 0, 0, 7, 8, 0, 0, 0, 1]
g8 = [0, 0, 5, 0, 0, 0, 8, 0, 0]

g = [g0, g1, g2, g3, g4, g5, g6, g7, g8]
game = Board(g)
game.solve()