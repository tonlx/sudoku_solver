import unittest
import solver

class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        g0 = [1,2,3,4,5,6,7,8,9]
        g1 = [4,5,6,7,8,9,1,2,3]
        g2 = [7,8,9,0,0,0,0,0,0]
        g3 = [2,3,4,0,0,0,0,0,0]
        g4 = [5,6,7,0,0,0,0,0,0]
        g5 = [8,9,1,0,0,0,0,0,0]
        g6 = [3,4,5,0,0,0,0,0,0]
        g7 = [6,7,8,0,0,0,0,0,0]
        g8 = [9,1,2,0,0,0,0,0,0]
        g = [g0, g1, g2, g3, g4, g5, g6, g7, g8]
        self.game = solver.Board(g)

    def test_done_across(self):
        self.assertTrue(self.game.done_across(0))
        self.assertTrue(self.game.done_across(1))
        self.assertFalse(self.game.done_across(2))
        self.assertFalse(self.game.done_across(3))


    def test_done_down(self):
        self.assertTrue(self.game.done_down(0))
        self.assertTrue(self.game.done_down(1))
        self.assertFalse(self.game.done_down(3))
    
    def test_done_square(self):
        self.assertTrue(self.game.done_square(0,0))
        self.assertTrue(self.game.done_square(0,2))
        self.assertTrue(self.game.done_square(1,1))
        self.assertTrue(self.game.done_square(1,0))
        self.assertTrue(self.game.done_square(2,2))
        self.assertFalse(self.game.done_square(3,4))
        self.assertFalse(self.game.done_square(5,7))
        self.assertFalse(self.game.done_square(6,3))
        

if __name__ == '__main__':
    unittest.main()