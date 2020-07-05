#!/usr/bin/python3
#coding:utf-8
from xml.etree.ElementTree import parse
tree = parse('XML_1_Write.xml')
root = tree.getroot()
QYT_Teachers = {}

for i in tree.iter(tag='teaching_ability'):
    Teachers_list = []
    for y in i.iter(tag='teacher'):
        Teachers_list.append(y.attrib['name'])
    QYT_Teachers[i.attrib['name']] = Teachers_list
print(QYT_Teachers)

QYT_Courses = {}

for i in tree.iter(tag='Subjects'):
    courses = []
    for y in i.iter(tag='SubjectName'):
        courses.append(y.attrib['name'])
    QYT_Courses[i.attrib['name']] = courses

print(QYT_Courses)