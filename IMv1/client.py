from time import sleep


import socket



hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
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

