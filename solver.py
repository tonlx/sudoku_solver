import math

class Board:
    
    RED = '\033[91m'
    ENDC = '\033[0m'
    size = 9

    def __init__(self, grid):
        self.grid = grid

    def done_across(self, row):
        nums = set()
        for col in range(Board.size):
            if self.grid[row][col] == 0:
                return False
            else:
                nums.add(self.grid[row][col])
        if len(nums) == Board.size:
            return True
        else:
            return False

    
    def done_down(self, col):
        nums = set()
        for row in range(Board.size):
            if self.grid[row][col] == 0:
                return False
            else:
                nums.add(self.grid[row][col])
        if len(nums) == Board.size:
            return True
        else:
            return False
    
    def done_square(self, row, col):
        small_size = int(math.sqrt(Board.size))
        nums = set()
        corner_row = int(row / small_size) * small_size
        corner_col = int(col / small_size) * small_size
        for row in range(small_size):
            for col in range(small_size):
                if self.grid[corner_row + row][corner_col + col] == 0:
                    return False
                else:
                    nums.add(self.grid[corner_row + row][corner_col + col])
        if len(nums) == Board.size:
            return True
        else:
            return False
            

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