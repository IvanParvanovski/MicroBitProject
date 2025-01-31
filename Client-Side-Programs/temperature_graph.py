#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np


# In[17]:


# Sample data
time_of_day = ['00:00', '06:00', '07:00', '12:00', '18:00', '24:00'] 
temperatures = [15, 20, 22, 25, 22, 18]

# Convert time strings to a format that can be plotted
# Here we use numpy to create a range of values for the x-axis
x = np.arange(len(time_of_day))


# In[19]:


print(x)


# In[ ]:


# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(x, temperatures, marker='o')

# Adding title and labels
plt.title('Temperature Throughout the Day')
plt.xticks(x, time_of_day)  # Set x-ticks to be the time of day
plt.xlabel('Time of Day')
plt.ylabel('Temperature (°C)')

# Show the plot
plt.grid()
plt.show()

