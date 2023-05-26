import json

# person = {"name": "John",
#            "age": 30, 
#            "city": "New York", 
#            "hasChildren": False, 
#            "titles": ["engineer", "programmer"]
#         }

# personJSON = json.dumps(person, indent=4, sort_keys=True)
# print(personJSON)

# # with open('person.json', 'w') as file_obj:
# #     json.dump(person, file_obj, indent=4)

# with open('person.json', 'r') as file_obj:
#     person = json.load(file_obj)
#     print(person)

# # convert from json to pythin dic
# person = json.loads(personJSON)
# print(person)
# Encode and Decode User class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)

# Convert to Json
userJSON = json.dumps(user)














