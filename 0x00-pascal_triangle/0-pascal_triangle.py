#!/usr/bin/python3
''' Pascal's Triangle '''


def pascal_triangle(num_rows):
    ''' Generate Pascal's Triangle '''
    if num_rows <= 0:
        return []

    # First row is always [1]
    triangle = [[1]]

    for i in range(1, num_rows):
        prev_row = triangle[-1]  # Get the last row
        # Start the new row with 1
        new_row = [1]

        # Each element is the sum of the two above it
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        # End the new row with 1
        new_row.append(1)
        triangle.append(new_row)

    return triangle
