from datetime import datetime

"""
Example:

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
}
"""


class TaskAction:

    def __init__(self, received_data):
        self.received_data = received_data
        self.time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.response_data = {}
        self.response_data.update({"time_stamp": self.time_stamp})

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

    def task_handler(self):
        try:
            if self.received_data["action"] == "sensors_initialization":
                self._initialization()
            elif self.received_data["action"] == "get_data_from_sensor":
                self._calibration(int(self.received_data["sensor_id"]))
            elif self.received_data["action"] == "get_state_of_all_sensors":
                self._get_state_of_all_sensors()
            elif self.received_data["action"] == "sensor_calibration":
                self._calibration(int(self.received_data["sensor_id"]))
            else:
                self._error_handler("action_error")
        except KeyError:
            self._error_handler("key_error")

        return self.response_data
