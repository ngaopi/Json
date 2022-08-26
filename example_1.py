#Convert dictionary to JSON array
import json
dict={"apple":3,"grapes":1}
array=[{"key":i,"value":dict[i]}for i in dict]
print(json.dumps(array))