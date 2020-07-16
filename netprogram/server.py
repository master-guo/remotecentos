#!/usr/bin/python3
#coding:utf-8
from socket import *
from threading import Thread
def single(c):
    while True:
        info = c.recv(1024)
        print("receive message",info.decode("utf-8"))
        message = input("input a message for send:")
        if message == 'q':
            break
        else:
            c.send(message.encode("utf-8"))

if __name__ == "__main__":
    server = socket(AF_INET,SOCK_STREAM)
    server.bind(('192.168.18.128',11111))
    server.listen(10)
    print("waiting for connection...")

    client,clientaddr = server.accept()
    print("connect to ",clientaddr)

    t1 = Thread(target=single,args=(client,))
    t1.start()
    t1.join()
