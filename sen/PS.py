import Adafruit_DHT
import RPi.GPIO as GPIO
import datetime
import time

class SensorAPI:
    """
    Class to measure temperature, humidity and distance from sensor to opstacle.
    Designed specialy for raspberry pi.
    """
    def __init__(self):
        self.initialize_all_sensors()
        self.temperature = ""
        self.humidity = ""
        self.distance = ""
        self.sensor_table = {"Temperature and Humindity": {"status": "active"},
                             "HC SR04": {"status": "active"}}
        self.initialize_all_sensors()

    def initialize_all_sensors(self):
        self.hcSr04_Init()

    def active_sensors(self):
        return self.sensor_table

    def getTempHumi(self,DHT11_pin=4, sensor=Adafruit_DHT.DHT11):
        """
        Get the data from sensor od Temperature and Humidity
        :param sensor: insert pin where is pluged in your sensor and type of sensoe
        DHT 11 or 22
        :return:
        Data with Temperature and Humidity
        """

        humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
        if humidity is not None and temperature is not None:
            return {"Temp": '{0:0.1f}*C'.format(temperature), "Humidity": '{0:0.1f}%'.format(humidity)}
            self.humidity = humidity
            self.temperature = temperature
        else:
            return {"Temp": None, "Humidity": None }


    def hcSr04_Init(self,TRIG = 21, ECHO = 20):
        """
        Init the HCSR04 sensor
        """
        # BCM numbering scheme
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # Set direction
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)


    def getDistance_Of_HcSr04Init(self,pinTrig=21, pinEcho=20):
        """
        Function to get the distance form opstacle to our sensor
        :param pinEcho: pin to Trigered, pin to get Data Echo
        :return: Distance from opstacle
        """
        # Pulse to start measure with HC-SR04
        GPIO.output(pinTrig, True)
        time.sleep(0.00001)
        GPIO.output(pinTrig, False)
        # Wait for HIGH on ECHO
        while GPIO.input(pinEcho) == 0:
            pulse_start = time.time()
        # wait for LOW again
        while GPIO.input(pinEcho) == 1:
            pulse_end = time.time()
        signalDelay = pulse_end - pulse_start
        # divider for uS to  s
        constDivider = 1000000 / 58
        distance = int(signalDelay * constDivider)
        return {"Distance": distance}

    def getData(self):
        tim = datetime.datetime.now()
        JSon = {"data":{"Time" : "{}".format(tim)}}
        JSon["data"].update(self.getDistance_Of_HcSr04Init())
        JSon["data"].update(self.getTempHumi())
        return JSon

if __name__ == '__main__':
    a = SensorAPI()
    try:
        print(a.getData())
        GPIO.cleanup()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()