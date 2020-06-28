#!/usr/bin/python3
#coding:utf-8
from data1 import alice,bob,tom
import shelve
db = shelve.open('people-shelve')
db['alice'] = alice
db['bob'] = bob
db['tom'] = tom
db.close()

