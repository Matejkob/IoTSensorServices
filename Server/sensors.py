import Adafruit_DHT
import RPi.GPIO as GPIO
import time


class SensorAPI:
    """
    Class to measure temperature, humidity and distance from sensor to obstacle.
    Designed for raspberry pi.
    """

    def __init__(self):
        self.response_data = {"data": {"dht11": {}, "hcsr04": {}}}

    def initialize_all_sensors(self):
        self.hcsr04_init(21, 20)
        self.get_data_from_dht11(4)
        if self.response_data["data"]["dht11"]["Temp"]:
            self.response_data["data"]["dht11"]["status"] = "active"
        else:
            self.response_data["data"].update({"errorCode": {"sensorError": "True"}})

        return self.response_data

    def get_data_from_dht11(self, pin_id):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin_id)

        if humidity is not None and temperature is not None:
            self.response_data["data"].update(
                {"dht11": {"Temp": '{0:0.1f}*C'.format(temperature), "Humidity": '{0:0.1f}%'.format(humidity)}})
        else:
            self.response_data["data"].update({"dht11": {"Temp": None, "Humidity": None}})

    def hcsr04_init(self, trig, echo):
        """
        Init the HCSR04 sensor
        """
        # BCM numbering scheme
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # Set direction
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        self.response_data["data"]["hcsr04"]["status"] = "active"

    def hcsr04_get_distance(self, trig, echo):
        # Pulse to start measure with HC-SR04
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        # Wait for HIGH on ECHO
        while GPIO.input(echo) == 0:
            pulse_start = time.time()
        # wait for LOW again
        while GPIO.input(echo) == 1:
            pulse_end = time.time()
        signal_delay = pulse_end - pulse_start
        # divider for uS to  s
        const_divider = 1000000 / 58
        distance = int(signal_delay * const_divider)
        self.response_data["data"]["hcsr04"]["distance"] = str(distance)

    def get_data_from_sensor(self):
        self.hcsr04_get_distance(21, 20)
        self.get_data_from_dht11(4)
        return self.response_data
