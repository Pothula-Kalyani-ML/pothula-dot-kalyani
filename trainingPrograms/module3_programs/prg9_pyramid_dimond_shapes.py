def pyramid_triangle(rows):
    if rows>1:
        line=1
        while(line<=rows):
            for i in range (rows-line):
                print(" ",end='')
            for i in range(line):
                if i==0 or i==line-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print('')
            line += 1
    else: print("not possible to print traingle in one line ")
def diamond_shape(rows):
    pyramid_triangle(rows)
    line=rows-1
    while(line>0):
        for i in range(rows-line,0,-1):
             print(" ",end='')
        for i in range(line):
            if i==0 or i==line-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")   
        print('')
        line -= 1
         
if __name__ =="__main__":
    n=int(input("enter number of rows : ")) 
    pyramid_triangle(n)
    diamond_shape(n)