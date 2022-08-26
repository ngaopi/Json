# Convert Text file to JSON in Python 
# Input :-
# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29
 
# Json_file.json:-
# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }
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

