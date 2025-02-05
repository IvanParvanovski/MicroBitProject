import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt 

tempIdealMin = 18
tempIdeal = 20
tempIdealMax = 30

humidityIdealMin = 50
humidityIdeal = 60
humidityIdealMax = 70

pressureIdealMin = 1000
pressureIdeal = 1010
pressureIdealMax = 1020

iaqScoreIdealMin = 0
iaqScoreIdeal = 0
iaqScoreIdealMax = 50

eC02IdealMin = 400
eC02Ideal = 700
eC02IdealMax = 1000

def main():
    global df
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
    xyParameter = (df["Time"].values,df["Humidity"].values)
    plt.xlabel("Time (s)")
    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Over Time")
    plt.plot(*xyParameter)
    plt.axhline(humidityIdealMin, color="red", linestyle = "--")
    plt.axhline(humidityIdeal, color="green", linestyle = "--")
    plt.axhline(humidityIdealMax, color="red", linestyle = "--")
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Over Time")
    plt.scatter(*xyParameter)
    plt.axhline(humidityIdealMin, color="red", linestyle = "--")
    plt.axhline(humidityIdeal, color="green", linestyle = "--")
    plt.axhline(humidityIdealMax, color="red", linestyle = "--")
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
    plt.axhline(pressureIdealMin, color="red", linestyle = "--")
    plt.axhline(pressureIdeal, color="green", linestyle = "--")
    plt.axhline(pressureIdealMax, color="red", linestyle = "--")
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("Pressure (hPa)")
    plt.title("Pressure Over Time")
    plt.scatter(*xyParameter)
    plt.axhline(pressureIdealMin, color="red", linestyle = "--")
    plt.axhline(pressureIdeal, color="green", linestyle = "--")
    plt.axhline(pressureIdealMax, color="red", linestyle = "--")
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
    plt.axhline(iaqScoreIdealMin, color="red", linestyle = "--")
    plt.axhline(iaqScoreIdeal, color="green", linestyle = "--")
    plt.axhline(iaqScoreIdealMax, color="red", linestyle = "--")
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("IQAScore")
    plt.title("IQAScore Over Time")
    plt.scatter(*xyParameter)
    plt.axhline(iaqScoreIdealMin, color="red", linestyle = "--")
    plt.axhline(iaqScoreIdeal, color="green", linestyle = "--")
    plt.axhline(iaqScoreIdealMax, color="red", linestyle = "--")
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
    plt.axhline(tempIdealMin, color="red", linestyle = "--")
    plt.axhline(tempIdeal, color="green", linestyle = "--")
    plt.axhline(tempIdealMax, color="red", linestyle = "--")
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
    plt.scatter(*xyParameter)
    plt.axhline(eC02IdealMin, color="red", linestyle = "--")
    plt.axhline(eC02Ideal, color="green", linestyle = "--")
    plt.axhline(eC02IdealMax, color="red", linestyle = "--")
    plt.show()

    plt.ylabel("eCO2Value (ppm)")
    plt.title("eCO2Value Boxplot")
    plt.boxplot(xyParameter[1])
    plt.show()

main()