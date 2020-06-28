import socket

host, port = ('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("the server is start")

while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("listening")

conn.close()
socket.close()
