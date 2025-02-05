import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt 


def main():
    global df
    global ideals
    ideals = get_ideals()
    df = initDB()
    show_DB()

    humidityVisualisation()
    pressureVisualisation()
    iaqScoreVisualisation()
    temperatureVisualisation()
    eC02Visualisation()

def readDB():
    return pd.read_csv("cleaned_data.csv")

def initDB():
    return readDB()

def show_DB():
    print(df.head(25))
    print(df.tail(25))
    print(df.info())
    for header in list(df.columns):
        print(df[header].describe())

def humidityVisualisation():
    xyParameter = (df["Time"],df["Humidity"])
    plt.xlabel("Time (s)")
    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Over Time")
    plt.plot(*xyParameter)
    plt.axhline(int(ideals[0][1]), color="red", linestyle = "--")
    plt.axhline(int(ideals[1][1]), color="green", linestyle = "--")
    plt.axhline(int(ideals[2][1]), color="red", linestyle = "--")
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Over Time")
    plt.scatter(*xyParameter)
    plt.axhline(ideals[0][1], color="red", linestyle = "--")
    plt.axhline(ideals[1][1], color="green", linestyle = "--")
    plt.axhline(ideals[2][1], color="red", linestyle = "--")
    plt.show()

    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Boxplot")
    plt.boxplot(xyParameter[1])
    plt.show()

def pressureVisualisation():
    xyParameter = (df["Time"].values,df["Pressure"].values)
    plt.xlabel("Time (s)")
    plt.ylabel("Pressure (hPa)")
    plt.title("Pressure Over Time")
    plt.plot(*xyParameter)
    plt.axhline(ideals[0][2], color="red", linestyle = "--")
    plt.axhline(ideals[1][2], color="green", linestyle = "--")
    plt.axhline(ideals[2][2], color="red", linestyle = "--")
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("Pressure (hPa)")
    plt.title("Pressure Over Time")
    plt.scatter(*xyParameter)
    plt.axhline(ideals[0][2], color="red", linestyle = "--")
    plt.axhline(ideals[1][2], color="green", linestyle = "--")
    plt.axhline(ideals[2][2], color="red", linestyle = "--")
    plt.show()

    plt.ylabel("Pressure (hPa)")
    plt.title("Pressure Boxplot")
    plt.boxplot(xyParameter[1])
    plt.show()

def iaqScoreVisualisation():
    xyParameter = (df["Time"].values,df["IQAScore"].values)
    plt.xlabel("Time (s)")
    plt.ylabel("IQAScore")
    plt.title("IQAScore Over Time")
    plt.plot(*xyParameter)
    plt.axhline(ideals[0][3], color="red", linestyle = "--")
    plt.axhline(ideals[1][3], color="green", linestyle = "--")
    plt.axhline(ideals[2][3], color="red", linestyle = "--")
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("IQAScore")
    plt.title("IQAScore Over Time")
    plt.scatter(*xyParameter)
    plt.axhline(ideals[0][3], color="red", linestyle = "--")
    plt.axhline(ideals[1][3], color="green", linestyle = "--")
    plt.axhline(ideals[2][3], color="red", linestyle = "--")
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("IQAScore")
    plt.title("IQAScore Boxplot")
    plt.boxplot(xyParameter[1])
    plt.show()

def temperatureVisualisation():
    xyParameter = (df["Time"].values,df["Temperature"].values)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (Celsius)")
    plt.title("Temperature Over Time")
    plt.scatter(*xyParameter)
    plt.axhline(ideals[0][0], color="red", linestyle = "--")
    plt.axhline(ideals[1][0], color="green", linestyle = "--")
    plt.axhline(ideals[2][0], color="red", linestyle = "--")
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (Celsius)")
    plt.title("Temperature Over Time")
    plt.scatter(*xyParameter)
    plt.axhline(ideals[0][0], color="red", linestyle = "--")
    plt.axhline(ideals[1][0], color="green", linestyle = "--")
    plt.axhline(ideals[2][0], color="red", linestyle = "--")
    plt.show()

    plt.ylabel("Temperature (Celsius)")
    plt.title("Temperature Boxplot")
    plt.boxplot(xyParameter[1])
    plt.show()

def eC02Visualisation():
    xyParameter = (df["Time"].values,df["eCO2Value"].values)
    plt.xlabel("Time (s)")
    plt.ylabel("eCO2Value (ppm)")
    plt.title("eCO2Value Over Time")
    plt.plot(*xyParameter)
    plt.axhline(ideals[0][4], color="red", linestyle = "--")
    plt.axhline(ideals[1][4], color="green", linestyle = "--")
    plt.axhline(ideals[2][4], color="red", linestyle = "--")
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("eCO2Value (ppm)")
    plt.title("eCO2Value Over Time")
    plt.scatter(*xyParameter)
    plt.axhline(ideals[0][4], color="red", linestyle = "--")
    plt.axhline(ideals[1][4], color="green", linestyle = "--")
    plt.axhline(ideals[2][4], color="red", linestyle = "--")
    plt.show()

    plt.ylabel("eCO2Value (ppm)")
    plt.title("eCO2Value Boxplot")
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
    
    for i in range(0,5):
        idealMins[i] = int(idealMins[i])
        idealsG[i] = int(idealsG[i])
        idealMaxs[i] = int(idealMaxs[i])

    return [idealMins,idealsG,idealMaxs]
main()