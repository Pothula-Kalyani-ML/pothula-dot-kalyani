def checkForKey(dataDict,searchKey):
    keys=dataDict.keys()
    if searchKey in keys:
        return True
    else: return False    
if __name__ == "__main__":
    sampleDict = {'name': 'John', 1: [2, 4, 3]}
    searchKey='name'  
    result=checkForKey(sampleDict,searchKey)
    if(result==True):
        print(" {} key already exists".format(searchKey))
    else:    
        print(" {} key does not exists".format(searchKey))
