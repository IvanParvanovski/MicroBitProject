from microbit import *
import radio
from bme688 import *
import OLED

# Assign a unique ID to each sensor Microbit (1, 2, 3, etc.)
SENSOR_ID = 2  # Change this for each Microbit

radio.on()
radio.config(channel=7)

init_sensor()
init_gas_sensor()

OLED.init_display()

# Display the sensor ID on the LED matrix
display.show(str(SENSOR_ID))

while True:
    read_data_registers()
    temperature = calc_temperature()
    pressure = calc_pressure()
    humidity = calc_humidity()
    light = display.read_light_level()
    
    data = "{},{},{},{},{},{}".format(SENSOR_ID, temperature, pressure, humidity, light, 0)  # 0 for CO2 as it's not instantly available
    
    radio.send(data)
    
    OLED.clear_display()
    OLED.show("ID: {}".format(SENSOR_ID), 0)
    OLED.show("Temp: {:.1f}C".format(temperature), 1)
    OLED.show("Hum: {:.1f}%".format(humidity), 2)
    OLED.show("Light: {}".format(light), 3)
    
    sleep(5000)

