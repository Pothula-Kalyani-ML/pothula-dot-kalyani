import numpy as arraynum


def matrix_z_form(matrix):
    matrix_z_form = []
    row, column = matrix.shape
    if row == column:
        for i in range(row):
            matrix_z_form.extend((matrix[0:1, i]))
        index = 1
        while(index < row-1):
            matrix_z_form.extend((matrix[index:index+1, row-(index+1)]))
            index += 1
        for i in range(row):
            matrix_z_form.extend((matrix[row-1:, i]))
    else:
        return " not possible to calculate because input matrix is not a square matrix"
    return matrix_z_form


if __name__ == "__main__":
    mat1 = arraynum.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    result1 = matrix_z_form(mat1)
    mat2 = arraynum.array([(5, 19, 8, 7),
                           (4, 1, 14, 8),
                           (2, 20, 1, 9),
                           (1, 2, 55, 4)])
    result2 = matrix_z_form(mat2)
    mat3 = arraynum.array([(1, 2, 3), (2, 3, 4)])
    result3 = matrix_z_form(mat3)
    print(result1)
    print(result2)
    print(result3)
