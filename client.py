# coding:utf-8
import socket

host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.connect((host, port))
    print("client is connected")
except ConnectionRefusedError:
    print("connection failed !")
finally:
    socket.close()

