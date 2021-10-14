import socket
 
"""
p = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
p.connect(('127.0.0.1',6688))
while 1:
    msg = input('please input')
    # 防止输入空消息
    if not msg:
        continue
    p.send(msg.encode('utf-8'))  # 收发消息一定要二进制，记得编码
    if msg == '1':
        break
p.close()
"""
class receiver:
    def __init__(self,host,port,buffer_size):
        self.port = port
        self.host = host
        self.buffer_size = buffer_size
        self.soc = None
        self.connected = False

    def connect(self):
        if not self.soc == None:
            print("Socket already existed")
            self.connected = True
            return   
        try:
            self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.soc.connect((self.host,self.port))
        except:
            print("Connection Failed")
        else:
            print("Success in connection")
            self.connected = True
    
    def disconnect(self):
        #self.soc.close()
        self.connected = False

    def regular_receive(self):
        if not self.connected:
            return
        msg = int(self.soc.recv(self.buffer_size).decode("utf-8"))
        return msg
