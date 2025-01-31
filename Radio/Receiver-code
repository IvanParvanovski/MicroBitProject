from microbit import *
import radio

radio.config(group=10)
radio.on()

ID = "MB1"

while True:
    msg = radio.receive()
    if msg and msg.startswith("MB1:"):
        display.scroll(msg[4:])