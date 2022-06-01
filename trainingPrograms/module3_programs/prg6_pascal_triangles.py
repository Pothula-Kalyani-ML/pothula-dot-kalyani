def nCr_calculate(n,r):
    fact_n=factorial_calculation(n)
    fact_r=factorial_calculation(r)
    fact_n_r=factorial_calculation(n-r)
    nCr=int(fact_n/(fact_r*fact_n_r))
    return nCr  
def factorial_calculation(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact   

def pascal_triangle(rows):
    line=0
    while(line<=rows):
        for i in range (rows-line):
            print("  ",end='')
        for i in range(line+1):
            value=nCr_calculate(line,i)
            if value<10:
                print(value,end="   ")
            else:
                print(value,end="  ")     
        print('')
        line += 1
if __name__ == "__main__":
    n=int(input())
    pascal_triangle(n)             




