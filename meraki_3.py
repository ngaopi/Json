# Q.3 write a python program to convert python object to json string.
import json
a={"ring":"nim","ja":"jo","lo":"ve","atta":"ullah"}
print(type(a))
b=json.dumps(a)
print(b)