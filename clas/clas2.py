#!/usr/bin/python3
#coding:utf-8
from clas1 import Person
class Manager(Person):
    def giveraise(self,percent,bonus=0.1):
        Person.giveraise(self,percent + bonus)

    def setJob(self,job):
        self.job = job

if __name__ == "__main__":
    guo = Manager("masterguo",41,20000,"it worker")
    print(guo.name,guo.job)
    guo.setJob("sellor")
    guo.setWife("limeiling")
    print(guo.job)
    print(guo.wife)
    print(guo.cheng(2,3))