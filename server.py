import socket

host, port = ('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("the server is start")

while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("listening...")

    # always mul of 2 like 1024 or 256
    data = conn .recv(1024)
    data = data.decode("utf8")
    print(data)

conn.close()
socket.close()
