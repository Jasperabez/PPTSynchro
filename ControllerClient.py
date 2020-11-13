import logging
from sys import platform

if platform == "linux":
    import pyxhook as pyhook
elif platform == "win32":
    import pythoncom
    import pyWinhook as pyhook

from config import *

if COMMS_TYPE == 'Wifi':
    from Handlers.SocketHandler import SocketHandler as CommsHandler
else:
    from Handlers.BtCommsHandler import BtCommsHandler as CommsHandler

keybind_funcs = {}
logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILE, 
                                                 encoding='utf-8')],
                    level=LOGGING_LEVEL)

def main():
    LoadKeysFromConfig()

    if COMMS_TYPE == 'Wifi':
        comms_socket = CommsHandler(CLIENT_HOST, CLIENT_PORT, SERVER_HOST, SERVER_PORT)
    else:
        comms_socket = CommsHandler(BT_SERVER_HOST, BT_SERVER_PORT, 'Client')
    comms_socket.Open()

    def OnKeyPress(event):
        print(event.Key)

        if event.Key in keybind_funcs.keys():
            keybind_funcs[event.Key](comms_socket)

        # if event.Key == "grave":
        #     new_hook.cancel()
        return True

    new_hook = pyhook.HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.HookKeyboard()

    try:
        if platform == "linux":
            new_hook.start()
        elif platform == "win32":
            pythoncom.PumpMessages()
    except KeyboardInterrupt:
        # User cancelled from command line.
        comms_socket.Close()
        pass
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        comms_socket.Close()
        msg = 'Error while catching events:\n  {}'.format(ex)
        pyhook.print_err(msg)
        logging.error(msg)

def AddKeybindFunc(key, func):
    keybind_funcs[key] = func

def NextSlideSend(comms_socket):
    comms_socket.SendMsg("next")
    print("NextSlideSend")

def PrevSlideSend(comms_socket):
    comms_socket.SendMsg("prev")
    print("PrevSlideSend")

def LoadKeysFromConfig():
    for next_key in NEXT_KEYS:
        AddKeybindFunc(next_key, NextSlideSend)
    for prev_key in PREV_KEYS:
        AddKeybindFunc(prev_key, PrevSlideSend)