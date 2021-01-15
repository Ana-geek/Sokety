from socket import *
from gui.server_window import ServerWindow


if __name__ == '__main__':
    ip = gethostbyname(gethostname())
    print(ip)

    server_win = ServerWindow()
    server_win.open()
