from time import sleep
import socket
from datetime import datetime
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Server: ", ip_address + " " + hostname)
# Create a socket.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to listen to a port.
serversocket.bind((ip_address, 9985))
# Tell the socket to start listening.
# The 10 is the maximum number of connections.
serversocket.listen(10)
num = 0
data = str
messages = []
connection, address = serversocket.accept()
# Setup an infinite loop so the socket will keep listening for
# incoming connections.
while not data == ip_address + ": close":
    # Read 1024 bytes of data from the connection.
    data = connection.recv(1024).decode()
    # Check the length of data. If the length is more than 0 then
    # that means something was sent, so print it out.
    if len(data) > 0:
        print("Message " + str(num) + ": " + data)
        f = open("messagelog.txt", "a+")
        now = datetime.now()
        f.write(str(now) + "   Message " + str(num) + ": " + data + "\n")
        num = num + 1
        connection, address = serversocket.accept()
        # If it gets a new connection, accept it and save the connection
connection, address = serversocket.accept()
# Close the socket.
print("client initiated shutdown")
serversocket.close()
f.close()

sleep(0.05)
