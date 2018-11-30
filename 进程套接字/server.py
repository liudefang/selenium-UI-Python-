# -*- encoding: utf-8 -*-
# @Time    : 2018/9/27 17:03
# @Author  : mike.liu
# @File    : server.py
from multiprocessing import Process
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def server(ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        p = Process(target=talk, args=(conn,))
        p.start()

    s.close()


if __name__ == '__main__':
    server('127.0.0.1', 8080)