#!/usr/bin/python3
#coding:utf-8
class Person:
    def __init__(self,name,age,salary=0,job=None):
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job

    def giveraise(self,percent):
        self.salary = self.salary * ( 1 + percent)

    def setWife(self,wife):
        self.wife = wife

    def cheng(self,x,y):
        return x*y