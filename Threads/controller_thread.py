from time import sleep
import pythoncom

from Handlers.PptHandler import PptHandler
from config import *

def ControllerThread(program_state, thread_lock, command_bind_funcs, comms_msg_queue):
    pythoncom.CoInitialize()
    slide_handler = PptHandler()

    while True:
        thread_lock.acquire()
        if program_state.isSet() and comms_msg_queue:
            msg = comms_msg_queue.pop(0)
            thread_lock.release()
            if (msg in command_bind_funcs.keys()) and (slide_handler.GrabPptSession()):
                command_bind_funcs[msg](slide_handler)
        else:
            thread_lock.release()