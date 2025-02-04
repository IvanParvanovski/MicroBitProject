#!/usr/bin/env python
# coding: utf-8

# In[5]:


import serial
import time
import csv


# In[17]:


import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
for port in ports:
    print(port)


# In[26]:


# Open the serial port (replace 'COM5' with the correct port for your OS)
ser = serial.Serial('/dev/cu.usbmodem1102', 115200, timeout=1)  # Adjust 'COM5' to your micro:bit's port
# On Linux or macOS, use something like '/dev/ttyUSB0' or '/dev/ttyACM0'

print(ser)

start_time = time.time()

with open("output.csv", mode="w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Time", "Temperature", "Humidity", "Pressure", "IQAScore", "eCO2Value"])
    
    print("Waiting for data...")

    while True:
        end_time = time.time()
        data = ser.readline().decode('utf-8').strip()
        
        print('whats going on')
        
        if end_time - start_time >= 5:
            break 
        
        if data:  
            print('Data received:' + data)  
            csv_writer.writerow(data.split(","))  # Write row to CSV

