#!/usr/bin/python3
#coding:utf-8
def banben():
    import sys
    return sys.platform

bb = banben()
if bb == 'win32':
    print("This is %s."%('windows'))
elif bb == 'linux':
    print("This is %s."%('linux'))
else:
    print('Unknow platform.')