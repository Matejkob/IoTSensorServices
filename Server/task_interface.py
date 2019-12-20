from datetime import datetime
from .server import SocketServer
from time import sleep

# python3 -m Server.task_interface.py  <------ to run task_interface.py

"""
----------------JSON COMMUNICATION MODEL--------------------
############################################################
Scenario_1:

client_request_dict = {

    'action': 'get_data_from_sensor',
    'sensor_id': '2'
    
}

server_response_dict = {

    'success flag': 'True',
    'time_stamp': '2019-12-05 19:16:01',
    'data_from_sensor_api': {
    (...)
    }
    'error': 'key_error' (FAILURE CASE)
}
############################################################
Scenario_2:

client_request_dict = {

    'action': 'sensor_initialization',
    'sensor_id': '2'
    
}

server_response_dict = {

    'success flag': 'True',
    'time_stamp': '2019-12-05 19:16:01',
    'data_from_sensor_api': {
    (...)
    }
    'error': 'key_error' (FAILURE CASE)
}
############################################################
Scenario_3:

client_request_dict = {

    'action': 'get_state_of_all_sensors',
    'sensor_id': 'all'
    
}

server_response_dict = {

    'success flag': 'True',
    'time_stamp': '2019-12-05 19:16:01',
    'data_from_sensor_api': {
    (...)
    }
    'error': 'key_error' (FAILURE CASE)
}
Scenario_4:

client_request_dict = {

    'action': 'sensor_calibration',
    'sensor_id': 'all'
    
}

server_response_dict = {

    'success flag': 'True',
    'time_stamp': '2019-12-05 19:16:01',
    'data_from_sensor_api': {
    (...)
    }
    'error': 'key_error' (FAILURE CASE)
}
"""


class TaskService(SocketServer):

    def __init__(self, port, private_key, server_interface_ip=""):
        self.time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.response_data = {}
        super().__init__(port, private_key, server_interface_ip)

    def _initialization(self):
        print("all sensor initialization")
        self.response_data.update({"success flag": "True"})
        # self.response_data.update({'data_from_sensor_api': METHOD_FROM_BARTEK_API})

    def _calibration(self, sensor_id):
        print("sensor calibration")
        self.response_data.update({"success flag": "True"})
        # self.response_data.update({'data_from_sensor_api': METHOD_FROM_BARTEK_API})

    def _get_data_from_sensor(self, sensor_id):
        print("getting data from sensor")
        sleep(3)
        self.response_data.update({"success flag": "True"})
        # self.response_data.update({'data_from_sensor_api': METHOD_FROM_BARTEK_API})

    def _get_state_of_all_sensors(self):
        print("getting state of sensors")
        self.response_data.update({"success flag": "True"})
        # self.response_data.update({'data_from_sensor_api': METHOD_FROM_BARTEK_API})

    def _error_handler(self, error_info):
        print("getting error info")
        self.response_data.update({"success flag": "False",
                                   "error": error_info
                                   })

    def clear_response_data(self):
        self.response_data = {}

    def update_dict_with_defaults(self):
        self.response_data.update({"time_stamp": self.time_stamp})

    def task_handler(self, received_data):
        try:
            if received_data["action"] == "sensors_initialization":
                self.update_dict_with_defaults()
                self._initialization()
            elif received_data["action"] == "get_data_from_sensor":
                self.update_dict_with_defaults()
                self._calibration(int(received_data["sensor_id"]))
            elif received_data["action"] == "get_state_of_all_sensors":
                self.update_dict_with_defaults()
                self._get_state_of_all_sensors()
            elif received_data["action"] == "sensor_calibration":
                self.update_dict_with_defaults()
                self._calibration(int(received_data["sensor_id"]))
            else:
                self.update_dict_with_defaults()
                self._error_handler("action_error")
        except KeyError:
            self.update_dict_with_defaults()
            self._error_handler("key_error")

        return self.response_data


server = TaskService(7555, "Adf#44fxc")
while True:
    print("Waiting for connection ... \n")
    server.accept_remote_handshake()
    request = server.rcv_data()
    resp = server.task_handler(request)
    server.send_data(resp)
    server.close_connection()
    server.clear_response_data()
