# Convert the following Vehicle Object into JSON
# import json
# class Vehicle:
#     def _init_(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
# Convert it into JSON format
# Expected Output:
# {
#     "name": "Toyota Rav4",
#     "engine": "2.5L",
#     "price": 32000
# }

    
import json
class Car:
    def __init__(self, brand, name, batch):
        self.brand = brand
        self.name = name
        self.batch = batch

  
# main function
if __name__ == "__main__":
  
    # create two new car objects
    c1 = Car("Honda", "city", "2005")
    c2 = Car("Honda", "Amaze", "2011")
  
    # convert to JSON format
    jsonstr3 = json.dumps(c1.__dict__)
    jsonstr4 = json.dumps(c2.__dict__)
  
    # print created JSON objects
    print(jsonstr3)
    print(jsonstr4)