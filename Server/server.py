import socket
from .data_ciphering import DataCiphering


class SocketServer:
    """Socket server class with symmetric ciphering"""

    def __init__(self, port, private_key, ip_address=""):
        """
        Create object which represent server instance with all default parameters. Also it bind local IP address of
        device and start listening to defined port.

        :param port: listening port of device
        :param private_key: security access key
        :param ip_address: interface ip address which will be bind to socket
        """
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ip_address = ip_address
        self.port = int(port)
        self.connection = None
        self.remote_con_params = ""
        self.sock.bind((self.ip_address, self.port))
        self.sock.listen(3)
        self.cipher = DataCiphering(private_key)

    def __del__(self):
        self.close_connection()

    def send_data(self, dictionary):
        """
        Send via socket connection.

        :param dictionary: input data to send through connection
        :return: None
        """
        byte_data = self.cipher.encrypt_dict(dictionary)
        self.connection.send(byte_data)

    def rcv_data(self):
        """
        Receive data via socket connection.

        :return: output data in dictionary format
        """
        dictionary = self.cipher.decrypt_dict(self.connection.recv(4096))
        return dictionary

    def accept_remote_handshake(self):
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
        Close connection with checking if client is actually connected.

        :return:
        """
        if self.connection:
            self.connection.close()
        elif self.sock:
            self.sock.close()
