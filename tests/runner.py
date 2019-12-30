import socket
from Server.data_ciphering import DataCiphering

# Run from terminal (in repo dir) ------ > python3 -m tests.runner.py

s = socket.socket()
port = 7555
s.connect(("IP", port))

client_request_dict_1 = {
    'action': 'get_data_from_sensor',
    'sensor_id': '4',
}

client_request_dict_2 = {
    'action': 'incorrect_action_string',
    'sensor_id': '4',
}

#############################################################################
# TestCase 1
#############################################################################
s.send(DataCiphering("Adf#44fxc").encrypt_dict(client_request_dict_1))
resp = s.recv(4096)
assert DataCiphering("Adf#44fxc").decrypt_dict(resp)["success flag"] == 'True'
assert not DataCiphering("Adf#44fxc").decrypt_dict(resp)["data"] == {}
print("TestCase 1 ----------> passed\n")
#############################################################################
# TestCase 2
#############################################################################
s.send(DataCiphering("Adf#44fxc").encrypt_dict(client_request_dict_2))
resp = s.recv(4096)
assert DataCiphering("Adf#44fxc").decrypt_dict(resp) == {}
print("TestCase 2 ----------> passed\n")
print("All TestCases Passed with success\n")
