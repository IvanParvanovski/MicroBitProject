#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[37]:


columns_to_read = ['Time', 'Temperature']
df = pd.read_csv('cleaned_data.csv', usecols=columns_to_read)

x = df['Time'] 


# In[31]:


print(list(df['Time']))
print(list(df['Temperature']))


# In[41]:


# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(x, df['Temperature'], marker='o')

# Adding title and labels
plt.title('Temperature Throughout the Day')
plt.xticks(x, list(df['Time']))  # Set x-ticks to be the time of day
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')

# Show the plot
plt.grid()
plt.show()

