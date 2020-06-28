#!/usr/bin/python3
#coding:utf-8
import sqlite3
conn = sqlite3.connect('masterguo1.db')
cursor = conn.cursor()
cursor.execute("create table test(id int,name varchar(20),age int)")
cursor.execute("insert into test values (1,'guoxiaogang',42)")
cursor.execute("insert into test values (2,'limeiling',43)")
cursor.execute("insert into test values (3,'guolingxuan',11)")
cursor.execute("select * from test")
yourresults = cursor.fetchall()
for i in yourresults:
    print(i)
cursor.execute("drop table if exists 'test';")
conn.commit()