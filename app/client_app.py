from socket import *
from gui.client_window import ClientWindow


if __name__ == '__main__':
    ip = gethostbyname(gethostname())
    print(ip)

    client_win = ClientWindow('Anna')
    client_win.open()
