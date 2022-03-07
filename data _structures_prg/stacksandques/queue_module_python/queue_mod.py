import queue
from stack_mod import *
if __name__ == "__main__":
    queue1=queue.Queue()
    print("select an action to be performed insert,delete,exit")
    while(1):
        action_on_queue=input("enter action to be perforemed :")
        if (action_on_queue=="insert"):
                elements_insertion(queue1)
        if(action_on_queue=="delete"):
                elements_deletion(queue1)
        if (action_on_queue=="exit"):
            break 
        if (action_on_queue != "insert" and action_on_queue != "delete" and action_on_queue !="exit"):
            print("have no selected relevant option")
    