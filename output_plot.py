import json

data = [{"name": "Nguyen Bao Huy", "age": 19, "city": "Quy Nhon"},{"name": "Nguyen Ha Thu Lan", "age": 19, "city": "Quy Nhon"}]
json_data = json.dumps(data, indent=4)
print(json_data)
