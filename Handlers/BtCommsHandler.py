import errno
import winerror
import socket
import logging
class BtCommsHandler:
    def __init__(self, server_mac_addr,server_port, role, comms_buff_size=1024):
        self.comms_buff_size = comms_buff_size
        self.server_port = server_port
        self.server_mac_addr = server_mac_addr
        self.role = role

    def Open(self):
        if self.role == 'Server':
            self.s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            self.s.bind((self.server_mac_addr, self.server_port))
            self.s.listen(1)
            self.ServerAccept()
            return True
        else:
            def ClientOpen(self):
                try:
                    self.s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
                    self.s.connect((self.server_mac_addr, self.server_port))
                    return True
                except OSError as err:
                    print(err)
                    if err.errno == 113:
                        return False
                    elif err.errno == errno.ECONNREFUSED:
                        return False
                    elif err.errno == errno.ECONNRESET:
                        return False
                    else:
                        logging.error(err)
                        raise OSError(err)
            while not ClientOpen(self):
                pass
            return True

    def ServerAccept(self):
        self.client_s, self.client_address = self.s.accept()
        return True

    def SendMsg(self, msg):
        if self.role == 'Server':
            try:
                self.client_s.send(msg.encode('utf-8'))
            except ConnectionResetError:
                self.client_s.close()
                self.ServerAccept()
                self.client_s.send(msg.encode('utf-8'))
        else:
            try:
                self.s.send(msg.encode('utf-8'))
            except (ConnectionResetError, ConnectionAbortedError) as err:
                self.Close()
                self.Open()
                self.s.send(msg.encode('utf-8'))

    def RecvMsg(self):
        if self.role == 'Server':
            data = self.client_s.recv(self.comms_buff_size)
            if not data:
                self.client_s.close()
                self.ServerAccept()
                data = self.client_s.recv(self.comms_buff_size)              
        else:
            if not data:
                self.Close()
                self.Open()
                self.s.recv(self.comms_buff_size)
        data = data.decode('utf-8')
        return data
    
    def Close(self):
        if self.role == "Server":
            self.client_s.close()
        self.s.close()