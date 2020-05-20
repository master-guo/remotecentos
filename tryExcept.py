#!/usr/bin/python3
#coding:utf-8
s = input('input some characters: ')
filename = 'a.txt'
try:
    fp = open(filename,'w+')
    print("%s read write mode open file sucess." %(filename))
    size = fp.write(s)
    print("%d byte write to %s"%(size,filename))
except IOError:
    print("%s open and write failure."%(filename))
finally:
    fp.close()