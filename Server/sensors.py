import Adafruit_DHT
import RPi.GPIO as GPIO
import time

def GetTempHumi(DHT11_pin = 4,sensor=Adafruit_DHT.DHT11):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
    return humidity,temperature

def HC_SR04_init(TRIG = 21,ECHO = 20):
    # BCM numbering scheme
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Set pins
    TRIG = 21
    ECHO = 20
    # Set direction
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def GetDistance(pinTrig=21,pinEcho=20):
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
