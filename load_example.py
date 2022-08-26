import json
b=open("load.json",)
data=json.load(b)
for i in data["emp"]:
    print(i)
b.close()
