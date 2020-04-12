#!/usr/bin/python3
#coding:utf-8
import random
pcc = ['石头','剪刀','布']
while True:
    pc = random.choice(pcc)
    mychoice = input('请出： ')
    if mychoice == pc:
        print('我也是出的%s,再来一次!'%(pc))
    elif pc =='石头' :
        if mychoice == '剪刀' :
            print('你输了，我出的是%s!'%(pc))
        elif mychoice == '布':
            print('你赢了，我出的是%s!'%(pc))
        elif mychoice == 'q':
            print('退出...')
            break
        else:
            print('您的输入有误！')
    elif pc == '剪刀':
        if mychoice == '石头':
            print('你赢了，我出的是%s!'%(pc))
        elif mychoice == '布':
            print('你输了，我出的是%s!'%(pc))
        elif mychoice == 'q':
            print('退出...')
            break
        else:
            print('您的输入有误！')
    elif pc == '布':
        if mychoice == '石头':
            print('你输了，我出的是%s!'%(pc))
        elif mychoice == '剪刀':
            print('你赢了，我出的是%s!'%(pc))
        elif mychoice == 'q':
            print('退出...')
            break
        else:
            print('您的输入有误！')
