def elements_insertion(arg):
        n=input(" select no.of elements to be entered:")
        for i in range(int(n)):
            arg.put(input())
        print("length of stack: ",arg.qsize())
        print("id of stack:",id(arg))


def elements_deletion(arg):       
    n=int(input(" select no.of elements to be deleted:"))
    list1=[]
    while ((not arg.empty()) and n!=0 ):
        list1.append(arg.get())
        n-=1
    print(list1)
    print("list address: " ,id(list1),"stack address: ",id(arg)) 
    print("length of stack after removing last element from stack: ",arg.qsize())
    if (arg.empty()):print("stack is empty")    