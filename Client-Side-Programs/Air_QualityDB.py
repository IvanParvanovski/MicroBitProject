import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates


def main():
    global databaseAQ
    databaseAQ = initDB()
    pd.set_option('display.max_rows', 100) 
    pd.set_option('display.max_columns', 100) 
    for i in range(2):
        add_dataValue()
    show_DB()


def initDB():
    try:
        return readDB()
    except:
        time,AQuality = get_dataValue()
        dataStructure = {"Air Quality" : [AQuality],
                         "TimeStamp"   : [time],
                         "DateTime" : [datetime.now()]}
        return pd.DataFrame(dataStructure)

def readDB():
    return pd.read_csv("Air_QualityDB.csv")

def get_dataValue():
    return (10,99)

def add_dataValue():
    time,AQuality = get_dataValue()
    dt = datetime.now()
    databaseAQ.loc[len(databaseAQ)] = { "Air Quality" : AQuality,
                                        "TimeStamp"   : time,
                                        "DateTime" : dt}

def show_DB():
    print(databaseAQ.head(25))
    print(databaseAQ.tail(25))
    print(databaseAQ.info())
    range = databaseAQ["Air Quality"].max() - databaseAQ["Air Quality"].min()
    print(range)
    print(databaseAQ["Air Quality"].describe())


def saveDB():
    pass;

main();