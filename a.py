#!/usr/bin/python3
#coding:utf-8
import random
def check_code():
    check_code = ''
    for i in range(4):
        current = random.randrange(0,4)
        if current != i:
            temp = chr(random.randint(65,90))
        else:
            temp = random.randint(0,9)
        check_code += str(temp)
    return check_code
while True:
    code = check_code()
    print(code)
    v1 = input('请输入验证码： ')
    if v1.upper() == code:
        print('ok,login now!')
        break
    else:
        print('sorry,retry!')
