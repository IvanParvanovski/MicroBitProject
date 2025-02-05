import serial
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
import time
import csv
import os

ser = serial.Serial('COM10', 115200, timeout=1)  # Adjust COM port as needed

# Dictionary to store data for each sensor and averages
data_store = defaultdict(lambda: {'timestamps': [], 'temperature': [], 'humidity': [], 'light': []})

def update_data_store(data):
    try:
        timestamp = datetime.now()
        sensor_id, temp, _, humidity, light, _ = map(float, data)
        sensor_id = int(sensor_id)
        
        data_store[sensor_id]['timestamps'].append(timestamp)
        data_store[sensor_id]['temperature'].append(temp)
        data_store[sensor_id]['humidity'].append(humidity)
        data_store[sensor_id]['light'].append(light)
        
        update_average_data()
    except ValueError as e:
        pass
    except IndexError as e:
        pass

def update_average_data():
    avg_data = data_store['average']
    avg_data['timestamps'] = []
    avg_data['temperature'] = []
    avg_data['humidity'] = []
    avg_data['light'] = []
    
    sensor_count = len(data_store) - 1  # Exclude the 'average' key
    if sensor_count > 0:
        max_length = max(len(data_store[s]['timestamps']) for s in range(1, sensor_count+1))
        for i in range(max_length):
            avg_data['timestamps'].append(data_store[1]['timestamps'][i])
            avg_data['temperature'].append(sum(data_store[s]['temperature'][i] for s in range(1, sensor_count+1) if i < len(data_store[s]['temperature'])) / sensor_count)
            avg_data['humidity'].append(sum(data_store[s]['humidity'][i] for s in range(1, sensor_count+1) if i < len(data_store[s]['humidity'])) / sensor_count)
            avg_data['light'].append(sum(data_store[s]['light'][i] for s in range(1, sensor_count+1) if i < len(data_store[s]['light'])) / sensor_count)

def create_graph():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle('Greenhouse Monitoring (Average)', fontsize=16, fontweight='bold')
    
    avg_data = data_store['average']
    
    if avg_data['timestamps']:
        # Light plot
        ax1.plot(avg_data['timestamps'], avg_data['light'], 'g-', label='Light', linewidth=2)
        ax1.set_ylabel('Light Level', fontweight='bold')
        ax1.set_ylim(0, max(avg_data['light']) * 1.1 if avg_data['light'] else 100)
        ax1.legend(loc='upper left')
        ax1.grid(True, linestyle='--', alpha=0.7)
        ax1.set_facecolor('#f0f0f0')
        
        # Temperature and Humidity plot
        ax2.plot(avg_data['timestamps'], avg_data['temperature'], 'r-', label='Temperature (°C)', linewidth=2)
        ax2.plot(avg_data['timestamps'], avg_data['humidity'], 'b-', label='Humidity (%)', linewidth=2)
        ax2.set_ylabel('Value', fontweight='bold')
        max_value = max(max(avg_data['temperature'] or [0]), max(avg_data['humidity'] or [0]))
        ax2.set_ylim(0, max_value * 1.1 if max_value else 100)
        ax2.legend(loc='upper left')
        ax2.grid(True, linestyle='--', alpha=0.7)
        ax2.set_facecolor('#f0f0f0')
        
        # Common x-axis label
        fig.text(0.5, 0.04, 'Time', ha='center', va='center', fontweight='bold')
        
        # Format x-axis ticks
        for ax in (ax1, ax2):
            ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S'))
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        plt.tight_layout()
        plt.draw()
        plt.pause(0.1)
        plt.close(fig)
    else:
        print("No data to plot yet.")

def save_to_csv():
    filename = 'sensor_data.csv'
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['timestamp', 'sensor_id', 'temperature', 'humidity', 'light']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        for sensor_id, sensor_data in data_store.items():
            if sensor_id != 'average' and sensor_data['timestamps']:
                latest_idx = -1
                writer.writerow({
                    'timestamp': sensor_data['timestamps'][latest_idx],
                    'sensor_id': sensor_id,
                    'temperature': sensor_data['temperature'][latest_idx],
                    'humidity': sensor_data['humidity'][latest_idx],
                    'light': sensor_data['light'][latest_idx]
                })

print("Waiting for data from the server...")

last_update_time = time.time()
last_csv_save_time = time.time()
update_interval = 10  # seconds
csv_save_interval = 60  # seconds

while True:
    try:
        data = ser.readline().decode().strip().split(',')
        if len(data) == 6:
            update_data_store(data)
            
            current_time = time.time()
            if current_time - last_update_time >= update_interval:
                create_graph()
                last_update_time = current_time
                
                # Print sensor data below the graph
                print("\nSensor Data:")
                for sensor_id, sensor_data in data_store.items():
                    if sensor_id != 'average' and sensor_data['timestamps']:
                        latest_idx = -1
                        avg_temp = sum(sensor_data['temperature']) / len(sensor_data['temperature'])
                        avg_humidity = sum(sensor_data['humidity']) / len(sensor_data['humidity'])
                        avg_light = sum(sensor_data['light']) / len(sensor_data['light'])
                        print(f"Sensor {sensor_id}: Temp: {sensor_data['temperature'][latest_idx]:.1f}°C  "
                              f"Humidity: {sensor_data['humidity'][latest_idx]:.1f}%  "
                              f"Light: {sensor_data['light'][latest_idx]}  ")
            
            if current_time - last_csv_save_time >= csv_save_interval:
                save_to_csv()
                last_csv_save_time = current_time
                print("Data saved to CSV file.")
        elif data != ['']:
            pass
    except Exception as e:
        print(f"Error: {e}")
