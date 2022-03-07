def elements_insertion(arg):
        n=input(" select no.of elements to be entered:")
        for i in range(int(n)):
            arg.append(input())
        print("elements: ",arg)


def elements_deletion(arg):       
    n=int(input(" select no.of elements to be deleted:"))
    choice=input("choose queue or stack:")

    list1=[]
    while ((len(arg)!=0) and n!=0 ):
        if(choice=="stack"):
            list1.append(arg.pop(-1))
            n-=1
        elif (choice=="queue"):
            list1.append(arg.pop(0))
            n-=1
        else:
            print("no relevant is made")
            break
        print("deleted elements: ",list1)
    if (len(arg)==0):print("stack is empty")    
    print("left out elements: ",arg)

    

if __name__ == "__main__":
    list_element=[]
    print("select an action to be performed insert,delete,exit")
    while(1):
        action_on_list=input("enter action to be perforemed :")
        if (action_on_list=="insert"):
            elements_insertion(list_element)
        if(action_on_list=="delete"):
            elements_deletion(list_element)
        if (action_on_list=="exit"):
            break
        if (action_on_list != "insert" and action_on_list != "delete" and action_on_list !="exit"):
          print("have not selected relevant option ")                   

