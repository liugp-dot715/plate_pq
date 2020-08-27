import os
from collections import defaultdict
import json

with open("./record.json", 'r') as load_f:
    load_dict = json.load(load_f)
print(len(load_dict.keys()))
for i in [1, 10, 50, 1000, 700, 90000, 1442, 565656, 797979, 2000000]:
    print(load_dict[list(load_dict.keys())[i]])


import requests
import json

a = requests.post('http://192.168.1.29:6788/nlu_engine/', json.dumps({"text": "明年端阳节下午五点半"})).json()
b = requests.post('http://192.168.1.29:6787/nlu/', json.dumps({"text": "明年端阳节下午五点半"})).json()
c = requests.post('http://192.168.1.29:1115/music/', json.dumps({"doc": "刘德华的七里香"})).json()
print(a)
print(b)
print(c)


