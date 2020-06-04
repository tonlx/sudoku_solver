import unittest
import solver

class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        g0 = [1,2,3,4,5,6,7,8,9]
        g1 = [4,5,0,7,0,9,1,0,3]
        g2 = [7,8,9,1,2,3,4,5,6]
        g3 = [2,3,4,5,6,7,8,9,1]
        g4 = [5,6,7,8,9,1,2,3,4]
        g5 = [8,9,1,2,3,4,5,6,7]
        g6 = [0,4,5,6,0,8,9,1,2]
        g7 = [6,0,8,9,1,2,3,4,5]
        g8 = [9,0,2,3,0,5,6,7,8]
        g = [g0, g1, g2, g3, g4, g5, g6, g7, g8]
        self.game = solver.Board(g)
        self.possible_options = {1,2,3,4,5,6,7,8,9}

    def test_check_across(self):
        self.assertEqual(self.game.check_across(self.possible_options, 1), {6,2,8})
    
    def test_check_down(self):
        self.assertEqual(self.game.check_down(self.possible_options, 4), {8,7,4})

    def test_check_square(self):
        self.assertEqual(self.game.check_square(self.possible_options, 6,2), {3,7,1})

    def test_get_options(self):
        self.assertEqual(self.game.get_options(6, 0), {3})

         

if __name__ == '__main__':
    unittest.main()