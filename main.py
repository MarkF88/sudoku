"""Represents a value on the Sudoku board, can either be an entered value or a clue
"""


class BaseSquare:
    """Base class for values on the board"""

    def __init__(self, value=None):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is not None:
            if value < 1 or value > 9:
                raise ValueError("Invalid Value")
        self._value = value

    @property
    def has_value(self):
        return self.value is not None


class ClueSquare(BaseSquare):
    """ Represents a clue on a Sudoku board, value cannot be changed once set"""

    @property
    def value(self):
        return self._value

    @BaseSquare.value.setter
    def value(self, value):
        if self.value is None:
            # For some reason this Syntax is required to overide a setter property
            super(ClueSquare, self.__class__).value.fset(self, value)
        else:
            raise ValueError("Cant set clue value once set")


class ValueSquare(BaseSquare):
    """Represents a guess on a Sudoku board, can be changed"""

    def __init__(self, value=None):
        super().__init__(value)
        self._is_error = False

    def clear_value(self):
        self._value = None

    @property
    def is_error(self):
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        self._is_error = is_error



class AreaChecker:
    """represents a line, column or area of nine squares and is used to check the compltion and correctness of an
    area"""
    def __init__(self):
        self.__squares = []

    def add_square(self, square):
        self.__squares.append(square)

    def set_error(self, square, value):
        if isinstance(square, ValueSquare):
            square.is_error = value


    def check_area(self):
        assert(len(self.__squares) ==9)
        found_values = {}
        for square in self.__squares:
            if square.has_value:
                if square.value in found_values:
                    self.set_error(square, True)
                    self.set_error(found_values[square.value], True)
                else:
                    self.set_error(square, False)
                    found_values[square.value] = square
            else:
                self.set_error(square, False)




class Board:
    """Contains all the Sudoku game board values"""

    def __init__(self):
        # Create the 9 by 9 list for the board values
        self.__values  = [[None] * 9 for i in range(9)]

        # Create all the areas to check
        self._section_areas = []
        self._row_areas = []
        self._column_areas = []

    def get_square(self, col, row):
        return self.__values[row - 1][col - 1]

    def _set_square(self, col, row, value):
        self.__values[row - 1][col - 1] = value

    def create_clue_square(self, col, row, value):
        square = ClueSquare(value)
        self._set_square(col, row, square)

    def create_value_square(self, col, row, value):
        square = ValueSquare(value)
        self._set_square(col, row, square)

    def get_value(self, col, row):
        return self.get_square(col, row).value

    def set_up_board(self, clues, values = None):
        """sets up a board with the previously entered values and clues"""
        self.set_up_clues(clues)
        #TODO Add code to enter the previosly set up values
        self.set_up_value_squares()

    def set_up_areas(self):
        """Create an rea for each 3*3 section of the board and each row and column"""


    def is_clue_square(self, col, row):
        square = self.get_square(col, row)
        if isinstance(square, ClueSquare):
            return True
        else:
            return False

    def set_up_clues(self, clues):
        # TODO Add code to check that all the values are here and the lengths are equal
        values = clues["values"]
        rows = clues["rows"]
        columns = clues["columns"]
        for x in range(len(values)):
            self.create_clue_square(columns[x], rows[x], values[x])

    def set_up_value_squares(self):
        """puts an empty value into each non-null square"""
        for row in self.__values:
            for x in range(len(row)):
                if row[x] is None:
                    row[x] = ValueSquare()


    def set_value(self, col, row, value):
        if self.is_clue_square(col, row):
            raise ValueError("Cant set Clue Square")


        """TODO Implement this
        when a value is set the following occurs
        Only set the value if the square is not a clue square
        We check all the rows columns and areas to see if they are completed or are in error, if in error then flag the
        squares that are in error.
        If they are all completed then we have a win and flag a win condition"""
        pass




if __name__ == '__main__':
    pass
