from Handlers.BtCommsHandler import BtCommsHandler
from config import *

def CommsThread(program_state, thread_lock, comms_msg_queue):
    comms_socket = BtCommsHandler(BT_SERVER_HOST, BT_SERVER_PORT, "Server")
    comms_socket.Open()

    while True:
        data = comms_socket.RecvMsg()
        if program_state.isSet():
            thread_lock.acquire()
            comms_msg_queue.append(data)
            thread_lock.release()