from microbit import *
from bme688 import *
import time

init_sensor()
init_gas_sensor()

print("Time,Temperature,Humidity,Pressure,IQAScore,eCO2Value")  # Print headers once

numOfReadings = 0
loop = True

while loop:
    # Read all data
    read_data_registers()
    temp = calc_temperature()
    humidity = calc_humidity()
    pressure = calc_pressure()  # Ensure pressure is calculated
    iaqScore, iaqPercent, eCO2Value = calc_air_quality()
   
    # Send data over serial in real time
    print("{},{},{},{},{},{}".format(str(numOfReadings * 5), str(temp), str(humidity), str(pressure), str(iaqScore), str(eCO2Value)))
   
    timeBefore = time.ticks_ms()
    numOfReadings += 1

    # Wait for 5 seconds, checking if button A is pressed to exit
    while time.ticks_diff(time.ticks_ms(), timeBefore) < 5000:
        if button_a.is_pressed() or (numOfReadings > 50):
            loop = False
            break
