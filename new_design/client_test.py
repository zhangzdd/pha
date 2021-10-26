import socket
import struct
import time
import matplotlib.pyplot as plt
import os
import multiprocessing
client = socket.socket()
def run_usb():
    os.system("usb_c.exe")
#p = multiprocessing.Process(target = run_usb)
#os.system("usb_c.exe")
time.sleep(5)
print("USB initiated")

ip_port = ("127.0.0.1", 6688)
while True:
    try:
        print("Try")
        client.connect(ip_port)
        print("Successful")
        break
    except:
        continue




while True:
    #data = client.recv(1024)
    #print(data.decode())
    #print(data.decode())
    command = input()
    client.send(command.encode())
    data = client.recv(1024*4)
    #print(data)
    #print(struct.unpack("i"*4096,data))
    tpl = struct.unpack("i"*1024,data)
    print(max(tpl))
    plt.plot(tpl)
    plt.show()
    plt.savefig("tmp.png")