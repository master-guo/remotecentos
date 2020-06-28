#!/usr/bin/python3
#coding:utf-8
import pickle
dbfile = open('people-pickle','rb')
msg = pickle.load(dbfile)
dbfile.close()
print(msg)
msg['alice']['salary'] *= 1.5
dbfile = open('people-pickle','wb')
pickle.dump(msg,dbfile)
dbfile.close()
print(msg)
# print(msg['alice']['name'])