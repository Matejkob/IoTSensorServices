from datetime import datetime
from .server import SocketServer
from .sensors import SensorAPI

# python3 -m Server.task_interface.py  <------ to run task_interface.py

"""
----------------JSON COMMUNICATION MODEL--------------------
############################################################
Scenario_1:

client_request_dict = {
    'action': 'get_data_from_sensor',
}

server_response_dict = {
    'successFlag': 'True',
    'timeStamp': '2019-12-05 19:16:01',
    'data': {
    
    
            
            }
    'error': 'key_error' (FAILURE CASE)
}
############################################################
Scenario_2:

client_request_dict = {
    'action': 'sensor_initialization',
}

server_response_dict = {
    'successFlag': 'True',
    'timeStamp': '2019-12-05 19:16:01',
    'data': {
              "dht11": { "Temp": (...), "Humidity": (...), "status": "active" },
              "hcsr04": {"distance": (...), "status": "active"}
            }
    'error': 'keyError' (FAILURE CASE)
}
"""


class TaskService(SocketServer):

    def __init__(self, port, private_key, server_interface_ip=""):
        self.time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.response_data = {}
        self.sensor_interface = SensorAPI()
        super().__init__(port, private_key, server_interface_ip)

    def _initialization(self):
        print("all sensor initialization")
        response_from_sensor = self.sensor_interface.initialize_all_sensors()
        if response_from_sensor:
            self.response_data.update(response_from_sensor)
            self.update_dict_with_task_information()
        else:
            self.update_dict_with_task_information(response_from_sensor['errorCode'])

    def _get_data_from_sensor(self):
        print("getting data from sensor")
        response_from_sensor = self.sensor_interface.get_data_from_sensor()
        if self.response_data:
            self.response_data.update(response_from_sensor)
            self.update_dict_with_task_information()
        else:
            self.update_dict_with_task_information(self.response_data['errorCode'])

    def clear_response_data(self):
        self.response_data = {}

    def update_dict_with_task_information(self, error_info=None):
        self.response_data.update({"timeStamp": self.time_stamp})
        if error_info:
            self.response_data.update({"successFlag": "False",
                                       "error": error_info})
        else:
            self.response_data.update({"successFlag": "True"})

    def task_handler(self, received_data):
        try:
            if received_data["action"] == "sensors_initialization":
                self._initialization()
            elif received_data["action"] == "get_data_from_sensor":
                self._get_data_from_sensor()
            else:
                self.update_dict_with_task_information("actionError")
        except KeyError:
            self.update_dict_with_task_information("errorCode")

        return self.response_data


# To test this code local go to repo dir ---> python3 -m Server.task_interface
# To test connect and get response from server ----> python3 tests/runner.py
server = TaskService(7555, "Adf#44fxc")
while True:
    print("Waiting for connection ... \n")
    server.accept_remote_handshake()
    request = server.rcv_data()
    resp = server.task_handler(request)
    server.send_data(resp)
    server.close_connection()
    server.clear_response_data()
