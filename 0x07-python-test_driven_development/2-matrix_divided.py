#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix that contains elements
    which are dividends of the division by the argument passed (div)
    All elements of the matrix are divided by div and
    rounded to 2 decimal places
    Raises:
        TypeError: if each row of the matrix is not of the same size
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if div is not a number (integer or float)
        ZeroDivisionError: if div is equal to 0
    """
    if div == 0:
        raise(TypeError("division by zero"))
    elif type(div) != int or type(div) != float:
        raise TypeError("div must be a number")
    elif len(matrix) < 2:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    else:

        length = len(matrix[0])
        new_matrix = [matrix[:] for matrix in matrix]
        for x in range(0, len(matrix)):
            if isinstance(matrix[x], list) is False:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            elif len(matrix[x]) != length:
                raise(TypeError("Each row of the matrix "
                                "must have the same size"))
            else:
                for y in range(0, len(matrix[x])):
                    if type(matrix[x][y]) == int or\
                       type(matrix[x][y]) == float:
                        new_matrix[x][y] = round((matrix[x][y]/div), 2)
                    else:
                        raise TypeError("matrix must be a matrix"
                                        "(list of lists) of integers/floats")
    return new_matrix
