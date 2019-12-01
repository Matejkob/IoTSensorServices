import socket
import json


class ServerJson:
    """
   Json socket server class to operate sending and receiving json data. How to use it:

    while True:
        print("wait for con ...")
        server.accept_request()
        data = server.rcv_json()
        print(data)
        server.send_json({"response": "msg received"}})
        server.close_connection()
    """

    def __init__(self, port, ip_address=""):
        """
        Create object which represent server instant with all default parameters. Also it bind local IP of device
        to socket and start listening to defined port.

        :param port: listening port of device
        """
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ip_address = ip_address
        self.port = port
        self.connection = None
        self.remote_con_params = ""
        self.sock.bind((self.ip_address, port))
        self.sock.listen(3)

    def __del__(self):
        self.close_connection()

    def send_json(self, dictionary):
        """
        Send json through socket.

        :param dictionary:
        :return: None
        """
        byte_data = json.dumps(dictionary).encode("utf-8")
        self.connection.send(byte_data)

    def rcv_json(self):
        """
        Receive json via socket connection.

        :return: dictionary
        """
        dictionary = json.loads(self.connection.recv(4096).decode("utf-8"))

        return dictionary

    def accept_request(self):
        """
        Accept remote connection on socket side.

        :return: None
        """
        if self.connection:
            self.close_connection()
        self.connection, self.remote_con_params = self.sock.accept()
        print("Connection from %s on port %d \n" % (self.remote_con_params[0], self.remote_con_params[1]))

    def close_connection(self):
        """
        Close connection with check if client is actually connected.

        :return:
        """
        if self.connection:
            self.connection.close()
        elif self.sock:
            self.sock.close()


server = ServerJson(7555)
while True:
    print("Waiting for connection ... \n")
    server.accept_request()
    data = server.rcv_json()
    print(data)
    server.send_json({"response": "example response data"})
    server.close_connection()
