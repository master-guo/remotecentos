#!/usr/bin/python3
#coding:utf-8
import argparse
def rt(a,b,c):
    print(a)
    print(b)
    print(c)

usage = "This command is used for return args."
pars = argparse.ArgumentParser(usage=usage)
pars.add_argument(nargs='?',dest='ip',help='ip address',type=str,default='1.1.1.1')
pars.add_argument("-f","--file",dest='filename',help='file name.',type=str)
pars.add_argument("-i","--interface",dest='interface',help='interface to run.',type=str,default='eth0')
args = pars.parse_args()

rt(args.ip, args.filename, args.interface)