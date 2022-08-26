# Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys
# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
# Expected Output:
# {
#     "age": 29,
#     "pd": 1,
#     "name": "value2"
# }
import json
a={
    "age": 29,
    "pd": 1,
    "name":2
}
c=json.dumps(a,indent=2,sort_keys=True)
print(c)