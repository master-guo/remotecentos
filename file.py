#!/usr/bin/python3
#coding:utf-8
import os,re,shutil
os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1.txt','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2.txt','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3.txt','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
files = os.listdir(os.getcwd())
for i in files:
    for lines in open(i,'r'):
        if re.match('.*qytang.*',lines):
            print('file %s is with python words.'%(i))
            open(i,'r').close()
            break
os.chdir('..')
shutil.rmtree('test')