#!/usr/bin/python3
#coding:utf-8
import re,os
route_n = os.popen("route -n")
# print(route_n.read())
line = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+UG',route_n.read())
print(line)
# for line in route_n:
# for line in route_n:
#     f = re.split('\s+',line)
#     # print(line)
#     if 'UG' in f:
#         print(f[1])
