#!/usr/bin/python3
#coding:utf-8
import os
path = r'/var/logss'
for dirpath,dirnames,filenames in os.walk(path):
    print(dirpath)
    # for filename in filenames:
    #     print(os.path.join(dirpath,filename))
pre_len = len(os.path.dirname(path))
print(os.path.dirname(path))
print(pre_len)