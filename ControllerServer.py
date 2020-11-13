import threading
import logging

from config import *

from Threads.toggle_thread import ToggleThread
from Threads.controller_thread import ControllerThread

if COMMS_TYPE == "Wifi":
    from Threads.comms_thread import CommsThread
else:
    from Threads.bt_comms_thread import CommsThread

command_bind_funcs = {}
comms_msg_queue = []
logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILE, 
                                                 encoding='utf-8')],
                    level=LOGGING_LEVEL)

def AddCommandBindFuncs(command, func):
    command_bind_funcs[command] = func

def NextPptSlide(slide_handler):
    print("pptnext")
    slide_handler.NextSlide()

def PrevPptSlide(slide_handler):
    print("pptprev")
    slide_handler.PrevSlide()

def main():
    AddCommandBindFuncs("next", NextPptSlide)
    AddCommandBindFuncs("prev", PrevPptSlide)
    program_state = threading.Event()
    thread_lock = threading.Lock()
    t1 = threading.Thread(name='toggle', 
                        target=ToggleThread,
                        args=(program_state, thread_lock))
    t2 = threading.Thread(name='controller', 
                            target=ControllerThread, 
                            args=(program_state, thread_lock, command_bind_funcs, comms_msg_queue))
    t3 = threading.Thread(name='comms',
                            target=CommsThread,
                            args=(program_state, thread_lock, comms_msg_queue))
    t1.start()
    t2.start()
    t3.start()
    program_state.set()

