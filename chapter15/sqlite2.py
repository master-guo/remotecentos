#!/usr/bin/python3
#coding:utf-8
import sqlite3,os
if os.path.exists("home_dict.db"):
    os.popen("rm -rf home_dict.db")
home_dict = [{"name":"masterguo","age":42,"salary":20000,"job":"security engineer"},
             {"name":"limeiling","age":43,"salary":4000,"job":"paotuide"},
             {"name":"guolingxuan","age":11,"salary":453,"job":"student"}]
conn = sqlite3.connect("home_dict.db")
cursor = conn.cursor()
cursor.execute("create table home(id int,name varchar(40),age int,salary int,job varchar(30))")
id = 1
for i in home_dict:
    name = i["name"]
    age = i["age"]
    salary = i["salary"]
    job = i["job"]
    cursor.execute("insert into home values (%d,'%s',%d,%d,'%s')" %(id,name,age,salary,job))
    id +=1
conn.commit()