#!/usr/bin/python3
#coding:utf-8
import os,re
ifconfig_result = os.popen("ifconfig" + ' ' + 'ens33').read()
print(ifconfig_result)
f = re.findall('(\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2})',ifconfig_result,re.M)
print(f)