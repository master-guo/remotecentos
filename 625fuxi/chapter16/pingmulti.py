#!/usr/bin/python3
#coding:utf-8
from scapy.all import *
from multiprocessing.pool import ThreadPool
from scapy.all import *
def pingone(x):
    ping_one_reply = sr1(IP(dst=x)/scapy.all.ICMP(),timeout=1,verbose=False)
    if ping_one_reply:
        return x
if __name__ == '__main__':
    pool = ThreadPool(150)

    results = []
    for i in range(1,254):
        argss = "192.168.18." + str(i)
        result = pool.apply_async(pingone,args=(argss,))
        results.append(result)
    pool.close()
    pool.join()
    k = []
    for i in results:
        #k.append(i.get())
        k.append(i.get())
    j = set(k)
    s = list(j)
    s.remove(None)
    print(s)


