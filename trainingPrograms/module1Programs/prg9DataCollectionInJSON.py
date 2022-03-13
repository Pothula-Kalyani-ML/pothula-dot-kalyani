
def DataCollectionInJSON(DATA):
    data=DATA.split("\n")
    resultStr=" "

    for line in data:
        line=line.strip()
        for index, lineData in enumerate(line):    # to eliminate spaces before and after colon
            dictstr=" "
            if lineData==":" :
                if line[index-1] ==" " and line[index+1]==" ": 
                    dictstr=line[:index-1]+":"+line[index+2:]
                    line=dictstr
        
        line=line.split(" ")
        for  lineData in line :                  # to copy contents before and after colon to a string       
            for lineDataContent in lineData: 
                if lineDataContent==":":
                    resultStr=resultStr+lineData+" "
    print(resultStr) 
    print('')     
    resultStr=resultStr.replace(',', '').replace('{', '').replace('}', '').replace('.','') # to omit other special characters in the string             
    print(resultStr)
    resultStr=resultStr.split()
    print('')     
    print(resultStr)


if __name__ == "__main__":
    DATA = '''Transaction completed. TxId:1, Custid:200. 
      Total service list for ep  {running:1, failed:0, stopped:0} tid:4664d973029f2fdb  trace:8ebca and span:None
      Unauthorized access user:root, ip:192.161.50.4
      Query : _docType:linux, _tag_app_Name:apm, _tag_project_Name:stack'''

    DataCollectionInJSON(DATA)