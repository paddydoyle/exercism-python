class Matrix(object):
    def __init__(self, matrix_string):
        if not matrix_string:
            return

        # Convert into a two-dimension array.
        # First split on '\n' to get the rows
        # Then split on ' ' to get the columns
        # And convert from string to int.
        self.rows = [[int(x) for x in row.split()]
                     for row in matrix_string.split('\n')]

    def row(self, index):
        """
        Return the given row of the matrix. Note that the
        'index' input starts at 1, not 0.
        """

        # Check bounds; it's easy to check the number of rows
        if index < 1 or index > len(self.rows):
            raise ValueError('Matrix row index out of bounds: {}'
                             .format(index))

        # Offset by 1 because we count from 0
        return self.rows[index-1]

    def column(self, index):
        """
        Return the given column of the matrix. Note that the
        'index' input starts at 1, not 0.
        """

        # Check bounds; calculate the minimum number of columns (to
        # avoid out of bounds errors)
        min_columns = min(len(r) for r in self.rows)

        if index < 1 or index > min_columns:
            raise ValueError('Matrix row index out of bounds: {}'
                             .format(index))

        # Offset by 1 because we count from 0
        column = [row[index-1] for row in self.rows]

        return column
