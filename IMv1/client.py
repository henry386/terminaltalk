from threading import Thread
from time import sleep

import socket


def func1():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    sleep(1)
    ipaddress = input("Enter ip Address to Connect To: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connected to: ", ipaddress)
    blanking = " "
    blanking = blanking.encode()
    s.connect((ipaddress, 9985))
    byt = "  connected from: " + hostname + " " + ip_address + "\n"
    byt = byt.encode()
    s.send(byt)
    s.close()
    while 1 == 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ipaddress, 9985))

        byt = input("Enter Message: ")
        if byt == "close":
            byt = ip_address + " Has left the chat" + "\n"
            byt = byt.encode()
            s.send(byt)
            s.detach()
            exit("Goodbye!")
        byt = ip_address + ": " + byt
        byt = byt.encode()
        s.send(byt)
        s.close()


def func2():
    from time import sleep
    import socket
    from datetime import datetime
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Server: ", ip_address + " " + hostname)
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ip_address, 9985))
    # The 10 is the maximum number of connections.
    serversocket.listen(10)
    num = 0
    data = str
    messages = []
    connection, address = serversocket.accept()

    while not data == ip_address + ": close":
        # Read 1024 bytes of data from the connection.
        data = connection.recv(1024).decode()
        if len(data) > 0:
            print("Message " + str(num) + ": " + data)
            f = open("messagelog.txt", "a+")
            now = datetime.now()
            f.write(str(now) + "   Message " + str(num) + ": " + data + "\n")
            num = num + 1
            connection, address = serversocket.accept()
    connection, address = serversocket.accept()
    # Close the socket.
    print("client initiated shutdown")
    serversocket.close()
    f.close()

    sleep(0.05)


if __name__ == '__main__':
    Thread(target=func1).start()
    Thread(target=func2).start()
