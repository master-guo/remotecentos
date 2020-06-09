#!/usr/bin/python3
#coding:utf-8
from clas1 import Person
class Manager(Person):
    def giveraise(self,percent,bonus=0.1):
        Person.giveraise(self,percent + bonus)

