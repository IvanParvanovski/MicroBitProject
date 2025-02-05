import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt 

def main():
    global df
    df = initDB()
    show_DB()
    humidityVisualisation()
    pressureVisualisation()
    iaqScoreVisualisation()

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
#graph 'Humidity', 'Pressure', 'IQAScore'
def humidityVisualisation():
    xyParameter = (df["Time"].values,df["Humidity"].values)
    plt.xlabel("Time (s)")
    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Over Time")
    plt.plot(*xyParameter)
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("Humidity (%RH)")
    plt.title("Humidity Over Time")
    plt.scatter(*xyParameter)
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
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("Pressure (hPa)")
    plt.title("Pressure Over Time")
    plt.scatter(*xyParameter)
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
    plt.show()

    plt.xlabel("Time (s)")
    plt.ylabel("IQAScore")
    plt.title("IQAScore Over Time")
    plt.scatter(*xyParameter)
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
    plt.show()

    plt.ylabel("eCO2Value (ppm)")
    plt.title("eCO2Value Boxplot")
    plt.boxplot(xyParameter[1])
    plt.show()

main()