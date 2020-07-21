#!/usr/bin/python3
#coding:utf-8
import paramiko,os
def guo_ssh(ip,username,password,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=port,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    # x = stdout.read().decode()
    # return x
    return stdout.read().decode()

if __name__ == '__main__':
    print(guo_ssh('192.168.18.128','root','redhat',22,'ls'))
    print(os.getcwd(),os.listdir())
