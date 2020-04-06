#!/usr/bin/python3
#coding:utf-8
from scapy.all import *
ping_one_reply = sr1(scapy.all.IP(dst='192.168.18.2')/scapy.all.ICMP(),timeout=1,verbose=False)
# ping_one_reply = sr1(IP(dst='192.168.18.2')/ICMP(),timeout=1,verbose=False)
ping_one_reply.show()


