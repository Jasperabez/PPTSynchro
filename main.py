from config import *

if __name__ == '__main__':
    try:
        if PROGRAM_MODE == 'Controller_server':
            import ControllerServer
            ControllerServer.main()
        if PROGRAM_MODE == 'Controller_client':
            import ControllerClient
            ControllerClient.main()
        else:
            import SniffKey
            SniffKey.main()
    except Exception as err:
        logging.error(err)