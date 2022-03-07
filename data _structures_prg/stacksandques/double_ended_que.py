from collections import deque
def elements_insertion(arg):
        n=input(" select no.of elements to be entered:")
        for i in range(int(n)):
            arg.append(input())
        print("elements: ",arg)
def elements_deletion_frontend(arg):       
    n=int(input(" select no.of elements to be deleted:"))
    list1=[]
    while ((len(arg)!=0) and n!=0 ):
        list1.append(arg.popleft())
        n-=1
    print(list1)
    if (len(arg)):print("stack is empty")    
    print("left out elements: ",arg)


def elements_deletion_rareend(arg):       
    n=int(input(" select no.of elements to be deleted:"))
    list1=[]
    while ((len(arg)!=0) and n!=0 ):
        list1.append(arg.pop())
        n-=1
    print(list1)
    if (len(arg)==0):print("stack is empty")    
    print("left out elements: ",arg)


if __name__ == "__main__":
    d_end_que=deque()
    print("select an action to be performed insert,dfront,drare,exit")
    while(1):
        action_on_stack=input("enter action to be perforemed :")
        if (action_on_stack=="insert"):
            elements_insertion(d_end_que)
        if(action_on_stack=="dfront"):
            elements_deletion_frontend(d_end_que)
        if(action_on_stack=="drare"):
            elements_deletion_rareend(d_end_que)
        if (action_on_stack=="exit"):
            break                     



