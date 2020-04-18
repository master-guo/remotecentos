#!/usr/bin/python3
#coding:utf-8
usrname = ['root','masterguo','masterxu']
passwd = ['123456','1qaz2wsx','nihao123!']
auth = dict(zip(usrname,passwd))
n = 0
while n<3:
    name = input('please input your name: ')
    passwod = input('and input your password: ')
    n+=1
    if name in auth.keys():
        if passwod == auth[name]:
            print('login correct!')
            stat = 'tr'
            break
        else:
            print('wrong input,retry now,%d times left!'%(3-n))
    else:
        print('wrong input,retry now,%d times left!'%(3-n))

while True:
    if stat == 'tr':
        print('''
        1. add user and set passwd
        2. delete user
        3. check user info.
        ''')
        choice = input('now,you can maintain user list,make a choice now: ')
        if choice == '1':
            newusr = input('input a newuser: ')
            while newusr not in usrname:
                passofusr = input("input password for newusr: ")
                retype = input("please retype the password: ")
                if passofusr == retype:
                    print('correct input,adding user now.')
                    usrname.append(newusr)
                    print(usrname)
                    passwd.append(passofusr)
                    print(passwd)
                    auth = dict(zip(usrname, passwd))
                    break
                else:
                    pass
            else:
                print('user %s has been exist.'%(newusr))
        elif choice == '2':
            newusr = input('input a user: ')
            while newusr in usrname:
                passofusr = input("password for usr: ")
                if passofusr == passwd[usrname.index(newusr)]:
                    print('correct input,deleting %s now.'%(newusr))
                    usrname.remove(newusr)
                    passwd.remove(passofusr)
                    break
                else:
                    print('password incorrect,')
                    newusr = input('input a newuser: ')
            else:
                print('user %s not exist.' % (newusr))
                newusr = input('input a newuser: ')
        elif choice == '3':
            newusr = input('input the user that you want to check: ')
            if newusr in usrname:
                print('the user is %s,and the password is %s'%(newusr,auth[newusr]))
            else:
                print('user %s does not exist.'%(newusr))

