#!/usr/bin/python3
#coding:utf-8
import base64
def b64_base64(x):
    y = bytes(x,'utf-8')
    y = str(base64.b64encode(y))[2:-1]
    return y
f = b64_base64('世界你好')

print(f)

def base64_b64(x):
    y = bytes(x,'utf-8')
    y = base64.b64decode(y)
    return y
k = base64_b64(f)
print(k.decode('utf-8'))