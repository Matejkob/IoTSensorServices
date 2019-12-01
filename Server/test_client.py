import socket
import json

s = socket.socket()
port = 7555
s.connect(("", port))

data = {
    "data": "some_data",
}

obj = json.dumps(data).encode("utf-8")
s.send(obj)
resp = s.recv(4096).decode("utf-8")
print(resp)
s.close()
