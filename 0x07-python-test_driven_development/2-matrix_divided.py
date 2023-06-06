#!/usr/bin/python3
"""
    module that has one function that
    devides all the elements of a matrix
    with a number
"""
def matrix_divided(matrix, div):
    """
    Devides all elements of a matrix by a given number 
    
    Args:
        matrix (list):list of lists containing integers or floats
        div (int or float): the number to divide the matrix elements with

    Returns:
        list: new matrix with elements divided by div

    Raises:
        TypeError:
            If the matrix is not a matrix (list of lists) of integers/floats,
            or if each row of the matrix does not have the same size.
        
        TypeError: If div is not a number (integer or float).
        
        ZeroDivisionError: If div is equal to zero.   
    """

    #validation of the div parameter
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("divison by zero")

        #validation of the matrix elements and structure
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(all(isinstance(number, (int, float)) for number in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
    new_matrix = []
    for row in matrix:
        # Check if each row has the same size as the first row
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        # Divide each element by div and round the result to 2 decimal places
        lists= [round(number / div, 2) for number in row]
        new_matrix.append(lists)


    return new_matrix
