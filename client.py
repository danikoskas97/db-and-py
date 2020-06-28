# coding:utf-8
import socket

host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.connect((host, port))
    print("client is now connected")

    data = "welcome iam the client"
    data = data.encode("utf8")
    socket.sendall(data)
    # sendall is to send all the data no lost

except ConnectionRefusedError:
    # if the server is not connected
    print("connection failed !")
finally:
    socket.close()
