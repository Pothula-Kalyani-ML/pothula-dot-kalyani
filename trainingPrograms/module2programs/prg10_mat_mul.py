def matrix_input():
    r = int(input("enter the number of rows:"))
    c = int(input("enter the number of column:"))
    matrix = []
    for i in range(r):
        a = []
        for j in range(c):
            print("enter elements row wise")
            a.append(int(input()))
        matrix.append(a)
    return matrix


def mat_multiplication(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        print("multiplication not possible")
        exit(1)
    #result_mat = [[0 for x in range(len(mat1))] for x in range(len(mat1[0]))]
    result_mat = [[0 for x in mat1], [0 for x in mat1[0]]]
    print(result_mat)
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result_mat[i][j] += mat1[i][k] * mat2[k][j]
    return result_mat


if __name__ == "__main__":
    matrix1 = matrix_input()
    matrix2 = matrix_input()
    result_matrix = mat_multiplication(matrix1, matrix2)
    print(result_matrix)
