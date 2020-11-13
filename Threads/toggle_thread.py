import pyWinhook as pyHook
import pythoncom
from win10toast import ToastNotifier

from config import *

def ToggleThread(program_state, thread_lock):
    def OnKeyPress(event):
        print(event.Key)

        if event.Key == TOGGLE_KEY:
            if program_state.isSet():
                program_state.clear()
                toaster.show_toast(APP_NAME, "Toggled OFF", threaded=True, duration=TOAST_SHOW_SEC)
            else:
                program_state.set()
                toaster.show_toast(APP_NAME, "Toggled ON", threaded=True, duration=TOAST_SHOW_SEC)

        return True

    toaster = ToastNotifier()
    new_hook = pyHook.HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.HookKeyboard()
    pythoncom.PumpMessages()