#from queue import PriorityQueue
import queue

def elements_insertion(arg):
        n=input(" select no.of elements to be entered:")
        for i in range(int(n)):
            arg.put((int(input("enter priority: ")),input("enter element:")))
        print("length of queue: ",arg.qsize())
    
def elements_deletion(arg):       
    n=int(input(" select no.of elements to be deleted:"))
    list1=[]
    while ((not arg.empty()) and n!=0 ):
        list1.append(arg.get())
        n-=1
    print(list1)        



if __name__ == "__main__":
    P_queue=queue.PriorityQueue()
    print("select an action to be performed insert,delete,exit")
    while(1):
        action_on_pqueue=input("enter action to be perforemed :")
        if (action_on_pqueue=="insert"):
                elements_insertion(P_queue)
        if(action_on_pqueue=="delete"):
                elements_deletion(P_queue)
        if (action_on_pqueue=="exit"):
            break      
        if (action_on_pqueue != "insert" and action_on_pqueue != "delete" and action_on_pqueue !="exit"):
            print(" have not selected relevant option")
