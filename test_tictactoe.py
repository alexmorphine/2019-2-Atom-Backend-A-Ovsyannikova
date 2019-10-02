import unittest
from TicTacToe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def test_TTT(self):
        ttt = TicTacToe('x')

        self.assertEqual(ttt.validate_input('1 2'), True)
        self.assertEqual(ttt.validate_input('12'), False)
        self.assertEqual(ttt.validate_m_n(1, 2), True)
        self.assertEqual(ttt.validate_m_n(10, 2), False)


if __name__ == '__main__':
    unittest.main()
