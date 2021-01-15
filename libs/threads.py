from threading import Thread
from libs.server import Server
from libs.client import Client
from tkinter import Label


class MyThread(Thread):
    def __init__(self, server: Server, label: Label):
        super().__init__()
        self.__server = server
        self.__label = label

    def run(self) -> None:
        self.__server.gui_work(self.__label)


class MyClientThread(Thread):
    def __init__(self, client: Client, label: Label):
        super().__init__()
        self.__client = client
        self.__label = label

    def run(self) -> None:
        self.__client.gui_work(self.__label)
