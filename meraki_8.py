# Q8.Tumhare pass four employes ki details hai list mai:-
# [“neelam”,”programer”,”24”,”2400”,]
# [“komal”,”trainer”,”24”,”20000”]
# [“anuradha”,”HR”,”25”,”40000”]
# [“Abhishek”,”manager”,”29”,”63000”]
# Visualize
# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.
# Output:-
# { 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }
import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","salary"]
r={}
s={}
t={}
u={}
v={}
i=0
while i<len(a):
    r[e[i]]=a[i]
    s[e[i]]=b[i]
    t[e[i]]=c[i]
    u[e[i]]=d[i]
    i=i+1
v["emp1"]=r
v["emp2"]=s
v["emp3"]=t
v["emp4"]=u
with open("meraki_8.json","w") as f:
    j=json.dump(v,f,indent=4)
    
