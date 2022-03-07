from queue import LifoQueue
import queue
from stacknque_mod_op import *



if __name__ == "__main__":
    stack1=queue.LifoQueue()
    print("select an action to be performed insert,delete,exit")
    while(1):
        action_on_stack=input("enter action to be perforemed :")
        if (action_on_stack=="insert"):
                elements_insertion(stack1)
        if(action_on_stack=="delete"):
                elements_deletion(stack1)
        if (action_on_stack=="exit"):
            break      
        if (action_on_stack != "insert" and action_on_stack != "delete" and action_on_stack !="exit"):
            print(" have not selected relevant option")
