#!/usr/bin/python3
#coding:utf-8
from scapy.all import *
def ping(a):
    pkt = IP(dst = a)/ICMP()
    return sr1(pkt,timeout=3,verbose=False)
if __name__ == "__main__":
    k = input('input a ip address for ping: ')

    if ping(k):
        print('it\'s ok!')
    else:
        print('it\'s not ok!')