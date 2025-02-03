import radio
from microbit import *
radio.config(channel=10,group=1)
radio.on()
uart.init(baudrate=115200)
while True:
    data = radio.receive() 
    if data is not None and data:
        uart.write(data+"\n")