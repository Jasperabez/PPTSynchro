from Handlers.SocketHandler import SocketHandler
from config import *

def CommsThread(program_state, thread_lock, comms_msg_queue):
    comms_socket = SocketHandler(SERVER_HOST, SERVER_PORT)
    comms_socket.Open()

    while True:
        data, addr = comms_socket.RecvMsg()
        if program_state.isSet():
            thread_lock.acquire()
            comms_msg_queue.append(data)
            thread_lock.release()