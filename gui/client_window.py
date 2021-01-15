from tkinter import *
from socket import *
from libs.client import Client
from libs.threads import MyClientThread


class ClientWindow(object):
    def __init__(self, name):
        self.__root = Tk()
        self.__frame = Frame(self.__root)
        self.__label = Label(self.__frame)
        self.__chat = Label(self.__frame)
        self.__host = gethostbyname(gethostname())
        self.__port = 9001
        self.__name = name
        self.__client = Client(self.__host, self.__port, self.__name)
        self.__client_thread = MyClientThread(self.__client, self.__chat)

    def config(self):
        self.__root.title('Clients module')
        self.__root.geometry('600x700')
        self.__root.resizable(True, False)
        self.__root.config(bg='#A69B8F')

        self.__label.config(bg='#A69B8F', text=str(self.__host), font='Helvetica 14 bold', fg='white')
        self.__chat.config(bg='#A69B8F', font='Helvetica 12', fg='#261D01', height=20, justify=LEFT, width=100)


    def layout(self):
        self.__frame.pack(padx=15, pady=15)
        self.__frame.config(bg='#A69B8F')
        self.__label.pack()
        self.__chat.pack()

    def open(self):
        self.config()
        self.layout()
        self.__client_thread.start()
        self.__root.mainloop()
