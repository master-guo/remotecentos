#!/usr/bin/python3
#coding:utf-8
import time,os,threading,random
from multiprocessing import Pool as ProcessPool
from multiprocessing.pool import ThreadPool


def multi(x,y,z):
    i = 1
    while i < 10:
        sum = x * y * z
        x += 1
        y += 1
        z += 1
        i += 1
        time.sleep(1)
    return (sum,os.getpid(),threading.currentThread().ident)

if __name__ == '__main__':
    pool = ThreadPool(5)

    results = []
    for i in range(0,10):
        x = random.randint(1,100)
        y = random.randint(1,100)
        z = random.randint(1,100)
        result = pool.apply_async(multi,args=(x,y,z))
        results.append(result)
    pool.close()
    pool.join()

    for i in results:
        print(i.get())

