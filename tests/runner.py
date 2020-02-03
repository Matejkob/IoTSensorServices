import socket
from Server.data_ciphering import DataCiphering

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
    'action': 'incorrect_action_string',
    'sensor_id': '4',
}

server_ip = "Here should be server ip"
port = 7555
#############################################################################
# TestCase 1
#############################################################################
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((server_ip, port))
s.send(DataCiphering("8x/A?D(G-KaPdSgVkYp3s6v9y$B&E)H@").encrypt_dict(client_request_dict_1))
resp_1 = DataCiphering("8x/A?D(G-KaPdSgVkYp3s6v9y$B&E)H@").decrypt_dict(s.recv(4096))
print("RECEIVED RESPONSE:")
print(resp_1)
s.close()
# assert resp_1["success flag"] == 'True'
# assert not resp_1["data"] == {}
# print("TestCase 1 ----------> passed\n")
# #############################################################################
# # TestCase 2
# #############################################################################
# s = socket.socket()
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.connect((server_ip, port))
# s.send(DataCiphering("Adf#44fxc").encrypt_dict(client_request_dict_2))
# resp_2 = DataCiphering("Adf#44fxc").decrypt_dict(s.recv(4096))
# print("RECEIVED RESPONSE:")
# print(resp_2)
# assert resp_2["success flag"] == 'False'
# assert resp_2["error"] == 'action_error'
# print("TestCase 2 ----------> passed\n")
# print("All TCs Passed with success\n")
