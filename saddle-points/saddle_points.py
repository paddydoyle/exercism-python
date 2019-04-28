def saddle_points(matrix):
    saddles = set()

    # Empty matrix?
    if not matrix:
        return saddles

    # Validate the matrix dimensions (unequal number of columns)
    if not validate(matrix):
        raise ValueError('Not a regular matrix')

    # Calc the dimensions.
    rows = len(matrix)
    cols = len(matrix[0])

    row_max = []
    for r in range(rows):
        row_max.append(max(matrix[r]))

    col_min = []
    for c in range(cols):
        col_min.append(min(row[c] for row in matrix))

    print("row_max = {}".format(row_max))
    print("col_min = {}".format(col_min))

    saddles = [(i+1, j+1) for i, r in enumerate(row_max)
               for j, c in enumerate(col_min)
               if r == c]

    print(">>>>>>>>>>>>.<<<<<<<<<< saddles = {}".format(saddles))

    saddles = [(r+1, c+1) for r in range(rows)
               for c in range(cols)
               if matrix[r][c] == row_max[r] and
                  matrix[r][c] == col_min[c]]

    print("<<<<<<<<<< saddles = {}".format(saddles))
    print("<<<<<<<<<< saddles = {}".format(saddles))
    print("<<<<<<<<<< saddles = {}".format(saddles))

    for row in matrix:
        row_max = max(row)
        print("\n>>>>>row = {}; max = {}".format(row, row_max))

        # List of all positions where the row_max occurs
        row_max_pos = [pos for pos, r in enumerate(row) if r == row_max]
        print("positions = {}".format(row_max_pos))

        for r in row_max_pos:
            # construct the column
            col = [row[r] for row in matrix]

            col_min = min(col)
            print("col for that = {}; min = {}".format(col, col_min))

            if (row_max == col_min):
                print("row_max == col_min")

                # List of all positions where the row_max occurs
                col_min_pos = [pos for pos, c in enumerate(col)
                               if c == col_min]
                print("positions = {}".format(col_min_pos))

                # Swap r and c to get the row and column numbers, and add
                # one to each since we are to start counting at 1, not 0.
                saddle = [(c + 1, r + 1) for c in col_min_pos
                          if matrix[r][c] == row_max]
                print("saddle = {}".format(saddle))

                saddles.update(saddle)
                print("<<<<<<<<<< saddles = {}".format(saddles))

    return saddles


def validate(matrix):
    # Check the lengths of each row (i.e. the number of columns).
    # Add them to a set and if the matrix is irregular, there
    # will be more than one value in the set.
    return len(set([len(row) for row in matrix])) == 1
