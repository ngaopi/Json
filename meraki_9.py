# Q.9 Apki pass ek shopping name ki ek dictionary hai
# Code Example
import json
list={
    "shoping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
item=input("enter the item:")
quantity=int(input("how much you want to buy?:"))
a=list["shoping_list"][item]
b=int(a)-quantity
list["shoping_list"][item]=b
print(list)