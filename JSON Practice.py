import json

# json_string = '''
# {
#   "students": [
#     {
#       "id": 1,
#       "name": "Tim",
#       "age": 21,
#       "full-time": true
#     },
#     {
#       "id": 2,
#       "name": "Joe",
#       "age": 33,
#       "full-time": false
#     }
#   ]
# }'''

# data = json.loads(json_string)
# data['test'] = True

# new_json = json.dumps(data, indent=4, sort_keys=True)
# print(new_json)
# #print(data['students'][0])

with open("data.json", "r") as f:
    data = json.load(f)

# #print(data.items())
# f.close()

with open("data2.json", "w") as f:
    json.dump(data, f)