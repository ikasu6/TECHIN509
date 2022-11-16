import unittest
from logic import make_empty_board, DisplayBoard, check_winner,play,P1vsP2,P1vsBot

board=[['O','O','O'], ['X','5','O'], ['X','O','X']]
win=check_winner(board,'O')
print(win)

# The test based on unittest module
class TestTicTactoeBoard(unittest.TestCase):
    def test_check_vertical(self):
        board=[['X','2','O'], ['X','5','O'], ['X','O','X']]
        self.assertEqual(check_winner(board,'X'), 'X', "X should win")

    def test_check_horizontal(self):
        board=[['O','O','O'], ['X','5','O'], ['7','X','X']]
        self.assertEqual(check_winner(board,'O'), 'O', "O should win ")

    def test_check_diagonal(self):
        board=[['O','X','X'], ['X','O','6'], ['7','8','O']]
        self.assertEqual(check_winner(board,'O'), 'O', "O should win ")   

    def test_check_nowin(self):
        board=[['O','X','X'], ['X','O','6'], ['7','O','9']]
        self.assertEqual(check_winner(board,'O'), None, "Nobody wins Yet ") 

    def test_check_draw(self):
        board=[['O','X','X'], ['X','O','O'], ['X','O','X']]
        self.assertEqual(check_winner(board,'O'), None, "Should be a draw")  

       



# run the test
if __name__ == '__main__':
    unittest.main()      