
def DataCollectionInJSON(DATA):

    data = DATA.split("\n")       #takes string DATA input
    resultStr = " "
    outputJson = {}

    for line in data:
        line = line.strip()     # to eliminate spaces before and after colon
        for index, lineData in enumerate(line):
            dictstr = " "
            if lineData == ":":
                if line[index-1] == " " and line[index+1] == " ":
                    dictstr = line[:index-1]+":"+line[index+2:]
                    line = dictstr

        line = line.split(" ")
        for lineData in line:                 # to copy contents before and after colon to a string
            for lineDataContent in lineData:
                if lineDataContent == ":":
                    resultStr = resultStr+lineData+" "
    
    resultStr = resultStr.replace(',', '').replace('{', '').replace('}', '').replace('.', '').replace("\\n'",'').replace("']",'')                   # to omit other special characters in the string
    resultStr = resultStr.split()

    resultList = []
    for i in resultStr:                  # removing duplicate items
        if i not in resultList:
            resultList.append(i)
    
    for index ,data in enumerate(resultList):
        
        count=0
        for  i in data:
            if i == ":":
                count+=1                 # removing double : in the list
        if count>1:
            dictstr = " "
            for index1, i in enumerate(data):
                if i == ":":
                    dictstr = data[index1+1:]     
                    break
            resultList[index]= dictstr
    
    for item in resultList:              # converting format from list to dict
            key, val = item.split(":")
            outputJson.update({key: val})
    return outputJson        
    


if __name__ == "__main__":
    data = open("prg9DataFile.txt", "r")
    DataStr=str(data.readlines())
    data.close()
    result=DataCollectionInJSON(DataStr)
    print(result)
