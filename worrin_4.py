# Exercise 5: Access the nested key ‘salary’ from the following JSON
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# # write code to print the value of salary
# Expected Output:
# 7000

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
a=json.loads(sampleJson)
print(type(a))
print(a)
print(a["company"]["employee"]["payable"]["salary"])
