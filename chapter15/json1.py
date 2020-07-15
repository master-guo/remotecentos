#!/usr/bin/python3
#coding:utf-8
import json
from dbfile import *

with open('m.json','w',encoding='utf-8') as f:
    json.dump(Teachers,f,ensure_ascii=False)
with open('m.json', 'r', encoding='utf-8') as f:
    k = str(json.load(f))
print(k)

dict_str = '{"qyt":[1,2,3]}'
list_str = '[1,2,3,"4"]'
bool_str = '{"qytang":true}'


dict1 = json.loads(dict_str)
list1 = json.loads(list_str)
bool1 = json.loads(bool_str)

print(type(dict1))
print(list1)
print(bool1)
