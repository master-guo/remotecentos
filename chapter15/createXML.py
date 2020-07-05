#!/usr/bin/python3
#coding:utf-8
from xml.dom.minidom import Document
doc = Document()
root = doc.createElement('root')
doc.appendChild(root)

QYT_Company = doc.createElement('company')
QYT_Company.setAttribute('name','qianyitang')
root.appendChild(QYT_Company)

Depart_Security = doc.createElement('department')
Depart_Security.setAttribute('name','security')
QYT_Company.appendChild(Depart_Security)

Depart_Description = doc.createElement('departmentDescription')
Depart_Security.appendChild(Depart_Description)

Depart_Description_Text = doc.createTextNode("\n\t\t\t\tmajor in security product and Curriculum Development of Cisco\n\t\t\t")
Depart_Description.appendChild(Depart_Description_Text)

Teachers = doc.createElement('teaching_ability')
Teachers.setAttribute('name','security group')
Depart_Security.appendChild(Teachers)

Teacher1 = doc.createElement('teacher')
Teacher1.setAttribute('name','masterguo')
Teachers.appendChild(Teacher1)

Teacher2 = doc.createElement('teacher')
Teacher2.setAttribute('name','masterli')
Teachers.appendChild(Teacher2)

Teacher3 = doc.createElement('teacher')
Teacher3.setAttribute('name','Mrs liu')
Teachers.appendChild(Teacher3)

Teacher4 = doc.createElement('teacher')
Teacher4.setAttribute('name','Mr ding')
Teachers.appendChild(Teacher4)

Subjects = doc.createElement('Subjects')
Subjects.setAttribute('name','Security CCNP')
Depart_Security.appendChild(Subjects)

Subjectsall = ['CCNASec','ACSS','Firewall','VPN','ISE','IPS','Secure']

for i in Subjectsall:
    Subject = doc.createElement('SubjectName')
    Subject.setAttribute('name',i)
    Subjects.appendChild(Subject)

XML_File = open('XML_1_Write.xml','w',encoding='utf-8')
XML_File.write(doc.toprettyxml(indent='    '))
XML_File.close()