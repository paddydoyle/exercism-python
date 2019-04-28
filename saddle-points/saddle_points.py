def saddle_points(matrix):
    # Empty matrix?
    if not matrix:
        return set()

    # Validate the matrix dimensions (unequal number of columns)
    if len(set([len(row) for row in matrix])) != 1:
        raise ValueError('Not a regular matrix')

    # Find the max values in each row.
    row_max_vals = []
    for r in range(len(matrix)):
        row_max_vals.append(max(matrix[r]))

    # Find the min values in each column.
    col_min_vals = []
    for c in range(len(matrix[0])):
        col_min_vals.append(min(row[c] for row in matrix))

    # Loop over the maxes and mins, and when they are equal we
    # add the indexes (plus 1, because it starts counting at 1, not 0)
    # as a tuple to the set.
    return set((i+1, j+1)
               for i, row_max in enumerate(row_max_vals)
               for j, col_min in enumerate(col_min_vals)
               if row_max == col_min)
