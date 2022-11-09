import unittest
from logic import check_winner

board=[['X','2','O'], ['X','5','O'], ['X','O','X']]
win=check_winner(board,'X')
print(win)

##Still working on this

'''class TestLogic(unittest.TestCase):
    def test_get_winner(self):
        board=[['X','2','O'], ['X','5','O'], ['X','O','X']]
        win= ()
        self.assertEqual(logic.check_winner(board,'X'),)'''