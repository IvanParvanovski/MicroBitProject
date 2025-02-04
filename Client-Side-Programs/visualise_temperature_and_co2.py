#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[95]:


columns_to_read = ['Time', 'Temperature', 'Humidity', 'Pressure', 'IQAScore', 'eCO2Value']
df = pd.read_csv('cleaned_data.csv', usecols=columns_to_read)


# In[54]:


print(list(df['Time']))
print(list(df['Temperature']))


# In[111]:


# Temperature 
x = df['Time'] 

plt.figure(figsize=(10, 5))
plt.plot(x, df['Temperature'], marker='o')

plt.title('Temperature since micro:bit activated')
plt.xticks(x, list(df['Time']))
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')

plt.grid()
plt.show()


# In[115]:


# CO2

plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['eCO2Value'], marker='o', linestyle='-', color='b')
plt.title('CO2 Levels ')
plt.xlabel('Time (seconds)')
plt.ylabel('eCO2 Value (ppm)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

