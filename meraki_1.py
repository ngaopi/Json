# write a program to convert json data to python object.
import json
a='{"d":23,"b":56,"c":"love you"}'
c=json.loads(a)
print(c)