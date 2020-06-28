#!/usr/bin/python3
#coding:utf-8
from data1 import dt
import pickle
dbfile = open('people-pickle','wb')
pickle.dump(dt,dbfile)
dbfile.close()