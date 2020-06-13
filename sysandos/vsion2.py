#!/usr/bin/python3
#coding:utf-8
class pc:
    def __init__(self):
        import sys
        self.banben = sys.platform

systm = pc()
bb = systm.banben
if bb == 'win32':
    print('This is %s.'%('Windows'))
else:
    print('This is not %s.'%('Windows'))
