
import re
outputJson={}
def DataToJson(dataStr):
    resultstr=''
    matches=re.findall(r'[\w.-]+:[\w.-]+',dataStr)
    for match in matches:
        resultstr=resultstr+match+' '
    print(resultstr)
    resultList=resultstr.split() 
    for item in resultList:              # converting format from list to dict
            key, val = item.split(":")
            outputJson.update({key: val})
    return outputJson 


if __name__ == "__main__":
    data = open("prg9DataFile.txt", "r")
    dataStr=str(data.read())
    outPut=DataToJson(dataStr)
    data.close()
    print(outPut)
