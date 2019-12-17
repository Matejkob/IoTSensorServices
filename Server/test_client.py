import socket
from .json_cipher import JsonCipher

s = socket.socket()
port = 7555
s.connect(("", port))

client_request_dict = {

    'action': 'get_data_from_sensor',
    'sensor_id': '2',
}

obj = JsonCipher("Adf#44fxc").encrypt_dict(client_request_dict)
s.send(obj)
resp = s.recv(4096)
print(JsonCipher("Adf#44fxc").decrypt_dict(resp))
s.close()
