import math
def print_g_patter(n):
    if n>2:
        no_of_line=1
        mid_line=math.ceil(n/2)
        while(no_of_line <= n):
            if no_of_line == 1 or no_of_line == n:
                print(" ",end='')
                for i in range(4):
                    print("*",end=" ")
                print(" ")
            elif no_of_line < mid_line :
                print("*")
            elif no_of_line >  mid_line :
                print("*\t*")
            elif no_of_line == mid_line :
                print("*",end='  ')
                for i in range(3):
                    print("*",end=" ")
                print('')
            no_of_line += 1
    else: return "not possible to print patter in lines less than 3"        

if __name__ == "__main__":
    lines_count=int(input())
    print_g_patter(lines_count)




            
    
