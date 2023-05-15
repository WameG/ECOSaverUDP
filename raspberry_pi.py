from sense_hat import SenseHat
from socket import *
import time
import json
from datetime import datetime

sense = SenseHat()

BROADCAST_TO_PORT=3520

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()

    data = {"id": 0, "humidity": humidity, "temperature": temperature, "date": str(datetime.now()).replace(" ", "T") + "Z"}

    s.sendto(json.dumps(data).encode(), ('<broadcast>', BROADCAST_TO_PORT))

    time.sleep(60)
