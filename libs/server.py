from socket import *
from time import ctime
from tkinter import Label


class Server(object):
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__address = (self.__host, self.__port)
        self.__listener = socket(AF_INET, SOCK_STREAM)

    def config(self):
        self.__listener.bind(self.__address)
        self.__listener.listen(15)

    def work(self):
        self.config()
        while True:
            # Ожидание запросов на подключение
            print('Server is waiting...')
            connect, client = self.__listener.accept()
            print(f"{ctime()}: request from {client} accepted")

            # Получение исходного сообщения от клиента:
            data = connect.recv(1024)
            mess = bytes.decode(data)
            # [Anas]>>>Hallo

            name = mess[1:mess.find('>>>')-1]
            text = mess[mess.find('>>>')+3:]
            print(f"{name} -> {text}")


            # Отправка подтверждения:
            response = f'Message from client: [{mess}] -> is sent'
            data = str.encode(response)
            connect.send(data)

            # Закрытие соединения:
            connect.close()
            if text == 'STOP_SERVER_01012000':
                print('Server stopped by Admin!')
                break


    def gui_work(self, label: Label):
        self.config()

        def _append_label_text(new_text: str):
            current_text = label.cget('text')
            current_text += '>>> ' + new_text + '\n'
            label.configure(text=current_text)

        while True:
            # Ожидание запросов на соединение:
            _append_label_text('Server is waiting...')
            connect, client = self.__listener.accept()
            _append_label_text(f'{ctime()}: request recieved from {client}')

            # Получение исходного сообщения от клиента:
            data = connect.recv(1024)
            mess = bytes.decode(data)
            # [Anas]>>>Hallo

            name = mess[1:mess.find('>>>') - 1]
            text = mess[mess.find('>>>') + 3:]
            _append_label_text(f"{name} -> {text}")


            # Отправка подтверждения:
            response = f'Client message: [{mess}] - sent'
            data = str.encode(response)
            connect.send(data)

            #  Закрытие соединения:
            connect.close()
            if mess == 'STOP_SERVER_01012000':
                print('Server stopped by Admin')
                break
