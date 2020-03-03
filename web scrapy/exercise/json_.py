import json

data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
with open('json_dumps_data.json', 'w') as file:
    file.write(json.dumps(data))

with open('json_dumps_data.json','w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))


data2 = [{"a": "A", "b": [1,6], "c": "C", ('d',): 'D'}]

print(json.dumps(data2, separators=(',', ':'), skipkeys=True))