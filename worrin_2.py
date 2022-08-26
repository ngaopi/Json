# PrettyPrint following JSON data
# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").
# sampleJson = {"key1": "value1", "key2": "value2"}
# Expected Output:
# {
#   "key1" = "value2",
#   "key2" = "value2",
#   "key3" = "value3"
# }
import json
a = {"key1": "value1", "key2": "value2"}
a["key3"]="value3"
c=json.dumps(a,indent=2,separators = (",","="))
print(c)
