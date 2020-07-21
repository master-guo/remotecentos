#!/usr/bin/python3
#coding:utf-8
import paramiko
import os, sys
import json
import time,datetime



def sshconfig(ip, port, username, password, cmd, PS1):
    # 实例化SSHClient
    client = paramiko.SSHClient()
    # 自动添加策略，保存服务器的主机名和密钥信息
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接SSH服务端，以用户名和密码进行认证
    client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
    chan = client.invoke_shell()
    chan.settimeout(9000)


    # 获取登陆后的消息
    welcomeinfo = ''
    while True:
        line = str(chan.recv(4096),encoding="utf-8")
        welcomeinfo += line
        if (PS1 is not None) & (len(PS1) > 0):
            isFindPS1 = False;
            for i in range(len(PS1)):
                if PS1[i] in line:
                    isFindPS1 = True
            if isFindPS1 == True:
                break;
    print(welcomeinfo)


    chan.send(cmd + '\n')
    result = ''
    # more交互处理
    more = 'More'
    more2 = '--More--'
    more3 = '<--- More --->'
    more4 = '---- More ----'
    #  循环获取数据
    time.sleep(1)
    while True:
        line2 = str(chan.recv(65535),encoding="utf-8")

        result += line2

        if (more in line2) | (more2 in line2) | (more3 in line2) | (more4 in line2):
            chan.send(" ")
            time.sleep(1)
            continue
        if (PS1 is not None) & (len(PS1) > 0):
            isFindPS1 = False;
            for i in range(len(PS1)):
                if PS1[i] in line2:
                    isFindPS1 = True
            if isFindPS1 == True:
                break

    print(result)
    return result

if __name__ == "__main__":
    k = sshconfig("192.168.101.10",22,"masterxu","a-o1cXrxga",'display cur','<NewF1-outside-1>')
    tm = datetime.datetime.now()
    recordtime = tm.strftime("%Y-%m-%d")
    filename = recordtime + "_" + "192.168.101.10" + ".config"
    file = open(filename,'w')
    file.write(k)
    file.close()
