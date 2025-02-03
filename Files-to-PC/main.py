from microbit import *
from bme688 import *
import time

init_sensor()
init_gas_sensor()

f = open("data.csv", "w")
# write headers
f.write("Time,Temperature,Humidity,Pressure,IQAScore,eCO2Value\n")
loop = True
display.show(Image.HAPPY)

numOfReadings = 0
while loop == True:
    # read all data
    read_data_registers()
    temp = calc_temperature()
    humidity = calc_humidity()
    pressure = calc_pressure()
    iaqScore, iaqPercent, eCO2Value = calc_air_quality()

    # write to file
    f.write("{},{},{},{},{},{}\n".format(str(numOfReadings * 5), str(temp), str(humidity), str(pressure), str(iaqScore), str(eCO2Value)))
    timeBefore = time.ticks_ms()

    numOfReadings += 1

    # wait for 5 secs - done like this so while we're waiting, we can still click the a button
    while time.ticks_diff(time.ticks_ms(), timeBefore) < 5000:

        if button_a.is_pressed() or (numOfReadings > 50):
            display.show(Image.DIAMOND)
            f.close()
            loop = False

            while True:
                if button_b.is_pressed():
                    uart.init(baudrate=115200)

                    f = open("data.csv", "r")
                    uart.write(f.read())
                    f.close()

            break