import unittest
import main


class TestSquareMethods(unittest.TestCase):

    def test_standard_create(self):
        clue = main.ClueSquare(1)

    def test_illegal_value_create(self):
        with self.assertRaises(ValueError):
            main.ClueSquare(0)

        with self.assertRaises(ValueError):
            main.ClueSquare(10)

    def test_clue(self):
        clue = main.ClueSquare(3)
        self.assertTrue(clue.value == 3)

        with self.assertRaises(ValueError):
            clue.value = 4

    def test_value(self):
        value = main.ValueSquare()
        value.value = 3
        self.assertTrue(value.value == 3)
        self.assertTrue(value.has_value)
        value.clear_value()
        self.assertTrue(value.value is None)

    def test_empty_board(self):
        board = main.Board()
        self.assertTrue(board.get_square(1, 1) is None)
        self.assertTrue(board.get_square(9, 9) is None)

    def test_board_set_values(self):
        board = main.Board()
        board.create_clue_square(1, 1, 3)
        board.create_value_square(1, 2, 3)
        self.assertTrue(board.get_square(1, 1).value == 3)
        self.assertTrue(board.get_square(1, 2).value == 3)

    def test_board_create(self):
        clues = {'values': [1, 2, 3], 'rows': [1, 2, 3], 'columns': [1, 1, 1]}
        board = main.Board()
        board.set_up_board(clues)
        self.assertTrue(board.get_square(1, 1).value == 1)
        self.assertTrue(board.get_value(1, 1) == 1)
        self.assertTrue(board.get_value(1, 2) == 2)

    def test_area_checker(self):
        # this area should result in an error at area[2,3] as they are the same Value and a value square
        area = [main.ClueSquare(1),
                main.ValueSquare(1),
                main.ValueSquare(3),
                main.ValueSquare(3),
                main.ValueSquare(5),
                main.ValueSquare(6),
                main.ValueSquare(7),
                main.ValueSquare(8),
                main.ValueSquare()]

        checker = main.AreaChecker()
        for x in area:
            checker.add_square(x)

        checker.check_area()

        self.assertTrue(area[1].is_error)
        self.assertTrue(area[2].is_error)
        self.assertTrue(area[3].is_error)
        self.assertFalse(area[8].is_error)
        self.assertFalse(area[7].is_error)

        # Change the values and recheck
        area[2].value = 2
        checker.check_area()
        self.assertTrue(area[1].is_error)
        self.assertFalse(area[2].is_error)
        self.assertFalse(area[3].is_error)
        self.assertFalse(area[8].is_error)
        self.assertFalse(area[7].is_error)

    def test_board_set_value(self):
        clues = {'values': [1, 2, 3], 'rows': [1, 2, 3], 'columns': [1, 1, 1]}
        board = main.Board()
        board.set_up_board(clues)
        board.set_value(2, 1, 1)
        board.set_value(2, 2, 2)
        board.set_value(2, 3, 1)
        self.assertTrue(board.get_square(2,1).is_error)
        self.assertTrue(board.get_square(2, 2).is_error)
        self.assertTrue(board.get_square(2, 3).is_error)
        board.set_value(2, 1, 2)
        self.assertFalse(board.get_square(2, 1).is_error)
