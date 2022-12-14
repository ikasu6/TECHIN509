import unittest
from logic import make_empty_board, check_winner,get_positions_onboard



# The test based on unittest module
class TestTicTactoeBoard(unittest.TestCase):
    def test_check_vertical(self):
        board=[['X',2,'O'], ['X',5,'O'], ['X','O','X']]
        self.assertEqual(check_winner(board,'X'), 'X', "X should win")

    def test_check_horizontal(self):
        board=[['O','O','O'], ['X',5,'O'], [7,'X','X']]
        self.assertEqual(check_winner(board,'O'), 'O', "O should win ")

    def test_check_diagonal(self):
        board=[['O','X','X'], ['X','O',6], [7,8,'O']]
        self.assertEqual(check_winner(board,'O'), 'O', "O should win ")   

    def test_check_nowin(self):
        board=[['O','X','X'], ['X','O',6], [7,'O',9]]
        self.assertEqual(check_winner(board,'O'), None, "Nobody wins Yet ") 

    def test_check_draw(self):
        board=[['O','X','X'], ['X','O','O'], ['X','O','X']]
        self.assertEqual(check_winner(board,'O'), None, "Should be a draw")  

    def test_check_display(self):
        board= [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(make_empty_board(), board, "board with positions should be returned") 

    def test_get_positions_onboard(self):
        board= [[1,2,3],[4,5,6],[7,8,9]]
        board2=[['X',2,3],[4,5,6],[7,8,9]]
        self.assertEqual(get_positions_onboard(board,1,'X'), board, "board with positions should be returned")   
        

       



# run the test
if __name__ == '__main__':
    unittest.main()      