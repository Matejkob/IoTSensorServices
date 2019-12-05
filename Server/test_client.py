import socket
import json

s = socket.socket()
port = 7555
s.connect(("", port))

client_request_dict = {

    'action': 'get_data_from_sensor',
    'sensor_id': '2'
}

obj = json.dumps(client_request_dict).encode("utf-8")
s.send(obj)
resp = s.recv(4096).decode("utf-8")
print(resp)
s.close()
