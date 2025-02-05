from microbit import *
import radio

radio.on()
radio.config(channel=7)
uart.init(baudrate=115200)

display.scroll("Server")

while True:
    message = radio.receive()
    if message:
        display.show("R")
        print(message)  # Send data over serial
        sleep(1000)
    else:
        display.show("S")
    sleep(100)
