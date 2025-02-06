import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt 
import matplotlib.dates as mdates

def main():
    global df
    global ideals
    ideals = get_ideals()
    df = initDB()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df[df["timestamp"].dt.date == df["timestamp"].iloc[- 1].date()]

    avgDB()
    show_DB()

    humidityVisualisation()
    temperatureVisualisation()

def readDB():
    return pd.read_csv("updated_sensor_data.csv")
def avgDB():
    global df
    time_l = df["timestamp"].tolist() 
    temp_l = df["temperature"].tolist()
    hmdy_l = df["humidity"].tolist()
    avgTimeList = []
    avgTempList = []
    avgHmdyList = []
    for i in range(len(time_l) -1):
        avgTimeList.append(time_l[i])
        avgTempList.append((temp_l[i] + temp_l[i+1]) /2)
        avgHmdyList.append((hmdy_l[i] + hmdy_l[i+1]) /2)
        i += 1
    df = pd.DataFrame({"timestamp":avgTimeList,"temperature":avgTempList,"humidity":avgHmdyList})
def initDB():
    return readDB()

def show_DB():
    print(df.head(25))
    print(df.tail(25))
    print(df.info())
    for header in list(df.columns):
        print(df[header].describe())

def humidityVisualisation():
    xyParameter = (df["timestamp"],df["humidity"])
    plt.xlabel("TimeStamp (Hours:Mins)")
    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Over Time")
    plt.plot(*xyParameter)
    plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
    plt.axhline(int(ideals[0][1]), color="red", linestyle = "--")
    plt.axhline(int(ideals[1][1]), color="green", linestyle = "--")
    plt.axhline(int(ideals[2][1]), color="red", linestyle = "--")
    plt.show()

    plt.xlabel("TimeStamp (Hours:Mins)")
    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Over TimeStamp")
    plt.scatter(*xyParameter)
    plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
    plt.axhline(ideals[0][1], color="red", linestyle = "--")
    plt.axhline(ideals[1][1], color="green", linestyle = "--")
    plt.axhline(ideals[2][1], color="red", linestyle = "--")
    plt.show()

    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Boxplot")
    plt.boxplot(xyParameter[1])
    plt.show()

def temperatureVisualisation():
    xyParameter = (df["timestamp"].values,df["temperature"].values)
    plt.xlabel("TimeStamp (Hours:Mins)")
    plt.ylabel("Temperature (Celsius)")
    plt.title("Temperature Over Time")
    plt.plot(*xyParameter)
    plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
    plt.axhline(ideals[0][0], color="red", linestyle = "--")
    plt.axhline(ideals[1][0], color="green", linestyle = "--")
    plt.axhline(ideals[2][0], color="red", linestyle = "--")
    plt.show()

    plt.xlabel("TimeStamp (Hours:Mins)")
    plt.ylabel("Temperature (Celsius)")
    plt.title("Temperature Over Time")
    plt.scatter(*xyParameter,marker="x")
    plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
    plt.axhline(ideals[0][0], color="red", linestyle = "--")
    plt.axhline(ideals[1][0], color="green", linestyle = "--")
    plt.axhline(ideals[2][0], color="red", linestyle = "--")
    plt.show()

    plt.ylabel("Temperature (Celsius)")
    plt.title("Temperature Boxplot")
    plt.boxplot(xyParameter[1])
    plt.show()

def get_ideals():
    idealMins = []
    idealsG = []
    idealMaxs = [] 

    with open("customIdeal.csv", "r") as file:
        file.readline()
        idealMins = file.readline()[4:].strip().split(',')
        idealsG = file.readline()[6:].strip().split(',')
        idealMaxs = file.readline()[4:].strip().split(',')
    
    for i in range(0,len(idealMins)):
        idealMins[i] = int(idealMins[i])
        idealsG[i] = int(idealsG[i])
        idealMaxs[i] = int(idealMaxs[i])

    return [idealMins,idealsG,idealMaxs]
main()
