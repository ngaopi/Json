# Access the value of key2 from the following JSON
# Expected Output:
# value2

import json
a= """{"key1": "value1", "key2": "value2"}"""
b=json.loads(a)
print(b["key2"])
