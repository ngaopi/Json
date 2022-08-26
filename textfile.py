# convert text file to json file
import json
a=open("textfile.txt","r")
b=a.read().split()
print(b)
c={}
i=0
while i<len(b)-1:
    c[b[i]]=b[i+1]
    i=i+2
print(c)
with open("textfile.json","w") as f:
    json.dump(c,f,indent=4)
a.close()

