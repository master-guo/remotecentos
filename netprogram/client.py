#!/usr/bin/python3
#coding:utf-8
from socket import *
from threading import Thread
def single(c):
    while True:
        message = input("input a message for sending:")
        if message == 'q':
            break
        else:
            c.send(message.encode("utf-8"))
        result = c.recv(1024)
        print("receive message ",result.decode("utf-8"))

if __name__ == "__main__":
    client = socket(AF_INET,SOCK_STREAM)
    client.connect(('192.168.18.128',11111))
    t1 = Thread(target=single,args=(client,))
    t1.start()
    t1.join()