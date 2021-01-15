from socket import *
from tkinter import Label


class Client(object):
    def __init__(self, host, port, name):
        self.__host = host
        self.__port = port
        self.__address = (self.__host, self.__port)
        self.__client = None
        self.__name = name

# Подсоединяемся к серверу
    def connect(self):
        if self.__client is None:
            self.__client = socket(AF_INET, SOCK_STREAM)
            self.__client.connect(self.__address)

    def work(self):
        while True:
            # Отправка смс
            mess = f"[{self.__name}]>>>" + input('Enter the message -> ')
            data = str.encode(mess)  # Кодируем инфу для отправки текст -> байты
            self.connect()
            self.__client.send(data)
            print('Sent.')

            # Ответ от сервера и его розкодировка
            data = self.__client.recv(1024)
            response = bytes.decode(data)
            print(response)

            # Освободить соединение и закрыть сокет
            self.__client.close()
            self.__client = None

            # Продолжать чат?
            stop = input('Want to procede? (y/n)')
            if stop == 'n':
                break

    def gui_work(self, label: Label):

        def _append_label_text(new_text: str):
            current_text = label.cget('text')
            current_text += '>>> ' + new_text + '\n'
            label.configure(text=current_text)

        while True:
            # Отправка смс
            mess = f"[{self.__name}]>>>" + input('Enter the message -> ')
            data = str.encode(mess)  # Кодируем инфу для отправки текст -> байты
            self.connect()
            self.__client.send(data)
            _append_label_text('Sent.')

            # Ответ от сервера и его розкодировка
            data = self.__client.recv(1024)
            response = bytes.decode(data)
            _append_label_text(response)

            # Освободить соединение и закрыть сокет
            self.__client.close()
            self.__client = None

            # Продолжать чат?
            stop = input('Want to procede? (y/n)')
            if stop == 'n':
                break
