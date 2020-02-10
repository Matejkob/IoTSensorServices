import socket
import json

# from Server.data_ciphering import DataCiphering

"""
Some Test Cases to check if our server is still working.
BEFORE RUN MODIFY SERVER_IP VALUE
TO RUN TESTS ------>>> python3 -m tests.runner.py (in repo dir)
"""

client_request_dict_1 = {
    'action': 'get_data_from_sensor',
    'sensor_id': '4',
}

client_request_dict_2 = {
    'action': 'sensors_initialization',
    'sensor_id': '4',
}

server_ip = "SERVER_IP"
port = 7555
#############################################################################
# TestCase 1
#############################################################################
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((server_ip, port))
s.send((json.dumps(client_request_dict_1)).encode("utf-8"))
resp = s.recv(4096).decode("utf-8")
resp_1 = json.loads(resp)
print("RECEIVED RESPONSE:\n")
print(resp)
s.close()
