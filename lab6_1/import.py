import json

with open("developers.json", 'r', encoding='UTF-8') as f:
 data = json.load(f)
print(data)