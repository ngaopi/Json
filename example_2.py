# convert dictionary to json quotes
import json
class fruits(dict):
    def str(self):
        return json.dumps(self)
collect=[['apple','grapes']]
result=fruits(collect)
print(result)