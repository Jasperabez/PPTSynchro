import logging
from sys import platform

if platform == "linux":
    import pyxhook as pyhook
elif platform == "win32":
    import pythoncom
    import pyWinhook as pyhook

from config import *

logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILE, 
                                                 encoding='utf-8')],
                    level=LOGGING_LEVEL)

def main():
    def OnKeyPress(event):
        print(event.Key)

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
        pass
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        msg = 'Error while catching events:\n  {}'.format(ex)
        pyhook.print_err(msg)
        logging.error(msg)