import Adafruit_DHT


def get_data_from_dht11(pin_id):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin_id)

    if humidity is not None and temperature is not None:
        return {"data": {"Temp": '{0:0.1f}*C'.format(temperature), "Humidity": '{0:0.1f}%'.format(humidity)}}
    else:
        return {"data": {"Temp": None, "Humidity": None}}
