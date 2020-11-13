import logging
import confuse

class MyConfiguration(confuse.Configuration):
    def config_dir(self):
        return './'

config_yaml = MyConfiguration('PPTController')

APP_NAME = config_yaml["APP_NAME"].get()
COMMS_TYPE = config_yaml["COMMS_TYPE"].get()
PROGRAM_MODE = config_yaml["PROGRAM_MODE"].get()
SERVER_HOST = config_yaml["WIFI_SOCKET_SERVER"]["HOST"].get()
SERVER_PORT = config_yaml["WIFI_SOCKET_SERVER"]["PORT"].get()
BT_SERVER_HOST = config_yaml["BT_SOCKET_SERVER"]["HOST"].get()
BT_SERVER_PORT = config_yaml["BT_SOCKET_SERVER"]["PORT"].get()
LOG_FILE = config_yaml["LOG_FILE"].get()
LOGGING_LEVEL = logging.getLevelName(config_yaml["LOGGING_LEVEL"].get())

if PROGRAM_MODE == "Controller_server":
    TOGGLE_KEY = config_yaml["CONTROLLER_SERVER"]["TOGGLE_KEY"].get()
    TOAST_SHOW_SEC = config_yaml["CONTROLLER_SERVER"]["TOAST_SHOW_SEC"].get()
elif PROGRAM_MODE == "Controller_client":
    CLIENT_HOST = config_yaml["CONTROLLER_CLIENT"]["WIFI_SOCKET_CLIENT"]["HOST"].get()
    CLIENT_PORT = config_yaml["CONTROLLER_CLIENT"]["WIFI_SOCKET_CLIENT"]["PORT"].get()
    NEXT_KEYS = config_yaml["CONTROLLER_CLIENT"]["NEXT_KEYS"].get()
    PREV_KEYS = config_yaml["CONTROLLER_CLIENT"]["PREV_KEYS"].get()





