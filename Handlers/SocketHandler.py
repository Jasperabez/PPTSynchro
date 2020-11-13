import socket

class SocketHandler:
    def __init__(self, own_host, own_port, server_host="", server_port=0, comms_buff_size=1024):
        self.own_host= own_host
        self.own_port = own_port
        self.server = (server_host, server_port)
        self.comms_buff_size = comms_buff_size
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def SendMsg(self, msg):
        self.s.sendto(msg.encode('utf-8'), self.server)

    def RecvMsg(self):
        data, addr = self.s.recvfrom(self.comms_buff_size)
        data = data.decode('utf-8')
        
        return(data, addr)

    def Open(self):
        self.s.bind((self.own_host,self.own_port))
    
    def Close(self):
        self.s.close()