#!/usr/bin/python3
#coding:utf-8
import sys,scapy.all
def testping(a):
    pkt = scapy.all.IP(dst = a)/scapy.all.ICMP()
    return scapy.all.sr1(pkt, timeout=3, verbose=False)
if testping(sys.argv[1]):
    print('%s is ok!'%(sys.argv[1]))
else:
    print('%s is not ok!'%(sys.argv[1]))