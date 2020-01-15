import Adafruit_DHT
import RPi.GPIO as GPIO
import time


# This code can be useful for standalone run but for our purpose it should return data
# in proper way ---> python dictionary based on JSON COMMUNICATION MODEL in file
# task_interface.py

# Functions should be placed in class (etc. SensorsAPI) as methods
# This class should contain methods based on below functions + methods from communication model
# You can consider if Scenario 4 is necessary
# Example class

# class SensorAPI:
#     def __init__(self):
#         self.temperature = ""
#         self.humidity = ""
#         self.distance = ""
#         self.sensor_table = {"sensor_name": {"status": "active"},
#                              "...": "..."
#                              }
#     methods for sensors services based on already done functions (...)
#     def get_data_from_sensor(self, sensor_id):
#         return {"..."}
#
#     def initialize_all_sensors(self):
#         return {"..."}
#
#     def get_state_of_all_sensors(self):
#         return {"..."}

# Can add more methods to get more data for Mateusz client App. It's better to have more in dictionary because finally
# he could get what he need without changes in your code
# Remember about PEP8 style
# When you finish this file you can modify task_interface.py and run runner.py

# you can do changes on other branch and create PR then review will be much easier for me :D


def getTempHumi(DHT11_pin=4, sensor=Adafruit_DHT.DHT11):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
    
    if humidity is not None and temperature is not None:
        return {"data": {"Temp": '{0:0.1f}*C'.format(temperature), "Humidity": '{0:0.1f}%'.format(humidity)}}
    else:
        return {"data": {"Temp": None, "Humidity": None}}


def hcSr04Init(TRIG=21, ECHO=20):
    # BCM numbering scheme
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Set pins
    TRIG = 21
    ECHO = 20
    # Set direction
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)


def getDistance(pinTrig=21, pinEcho=20):
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
    return distance


def main():
    HC_SR04_init()
    print(GetDistance())
    print(GetTempHumi())
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
