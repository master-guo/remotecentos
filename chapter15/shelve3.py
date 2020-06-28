#!/usr/bin/python3
#coding:utf-8
import shelve
db = shelve.open('people-shelve')
alice = db['alice']
alice['salary'] *= 1.5
db['alice'] = alice
db.close()