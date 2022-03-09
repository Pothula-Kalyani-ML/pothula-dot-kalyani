vowels = ['a','e','i','o','u']

output=[]
result=[]
count=0
for l in vowels:
    vowels.extend(l)
    vowels.remove(l)
    for k in vowels[1:]:
        vowels.extend(k)
        vowels.remove(k)
        for j in vowels[2:]:
            vowels.extend(j)
            vowels.remove(j) 
            for i in vowels[3:]:
                vowels.extend(i)
                vowels.remove(i)
                output.extend(vowels)
                result.append(vowels[:5])
                count+=1
    
print(count)   
#print(output)
print(result)
                  