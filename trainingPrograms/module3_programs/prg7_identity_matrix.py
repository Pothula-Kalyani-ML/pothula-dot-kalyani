if __name__=="__main__":
    n=int(input("enter the order of matrix: "))
    result_mat = [[0 for x1 in range(n)] for x2 in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                result_mat[i][j]=1
    print(result_mat)            
