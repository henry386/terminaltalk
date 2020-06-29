import socket
from time import sleep
from tkinter import *
from tkinter import messagebox, scrolledtext
from tkinter.scrolledtext import *
from tkinter.ttk import *

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

def connect(ipaddress,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        blanking = " "
        blanking = blanking.encode()
        s.connect((ipaddress, port))
        byt = "  Connected from: " + hostname + " " + ip_address + "\t"+str(port)+"\n"
        byt = byt.encode()
        s.send(byt)
        s.close()
    except socket.error as exc:
        messagebox.showerror("Socket Connection Error",exc)

def chat(ipaddress,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ipaddress, port))
        byt = messageentry.get("1.0",'end-1c')
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
        messageview.insert(END,messageentry.get("1.0",'end-1c')+"\n\n")
        messageview.see("end")
        messageentry.delete("1.0",END)
        messageentry.focus_set()
    except socket.error as exc:
        messagebox.showerror("Socket Connection Error",exc)

root = Tk()
root.geometry("400x600+600+30")
root.title("Terminal Talk - Client")
root.resizable(False, False)

iplabel = Label(root, text="Enter Server IP : ")
iplabel.place(x=5,y=5)

ipaddr = StringVar()
ipaddr.set("192.168.43.170")

ipentry = Entry(root, width=17, textvariable=ipaddr)
ipentry.place(x=95,y=5)

iplabel = Label(root, text="Port : ")
iplabel.place(x=210,y=5)

portno = IntVar()
portno.set(9985)

portnumber = Entry(root, width=8, textvariable=portno)
portnumber.place(x=250,y=5)

ipbutton = Button(root, text="CONNECT", command=lambda:connect(ipaddr.get(), portno.get()))
ipbutton.place(x=315,y=3)


messageview = ScrolledText(root, width=47, height=29)
messageview.place(x=5, y = 33)

messageentry = ScrolledText(root, width=35, height=5)
messageentry.place(x=5,y=510)

messagebutton = Button(root, text="SEND", command=lambda:chat(ipaddr.get(), portno.get()))
messagebutton.place(x=320,y=540)

messageview.insert(END, "\tTERMINAL TALK   -   CLIENT\n\t--------------------------\n")
for i in range(1,27):
    messageview.insert(END,"\n")
root.mainloop()
