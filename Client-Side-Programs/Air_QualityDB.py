import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

databaseAQ = pd.DataFrame()

def main():
    global databaseAQ
    databaseAQ = initDB()
    pd.set_option('display.max_rows', 100) 
    pd.set_option('display.max_columns', 100) 
    for i in range(2):
        add_dataValue()
    graphDB()
    show_DB()


def initDB():
    try:
        return readDB()
    except:
        time,AQuality = get_dataValue()
        dataStructure = {"Air Quality" : [AQuality],
                         "TimeStamp"   : [time],
                         "DateTime" : [str(datetime.now())]}
        return pd.DataFrame(dataStructure)

def readDB():
    return pd.read_csv("Air_QualityDB.csv")

def get_dataValue():
    return (10,99)

def add_dataValue():
    time,AQuality = get_dataValue()
    databaseAQ.loc[len(databaseAQ)] = { "Air Quality" : AQuality,
                                        "TimeStamp"   : time,
                                        "DateTime" : str(datetime.now())}
def show_DB():
    print(databaseAQ.head(25))
    print(databaseAQ.tail(25))
    print(databaseAQ.info())
    range = databaseAQ["Air Quality"].max() - databaseAQ["Air Quality"].min()
    print(range)
    print(databaseAQ["Air Quality"].describe())


def graphDB():
    pointAmount = 100
    x= databaseAQ["DateTime"].tail(pointAmount)
    y= databaseAQ["Air Quality"].tail(pointAmount)
    fig, ax = plt.subplots()  
    #ax.plot(x, y, marker='o', label="Data Points")
    line, = ax.plot(x, y, lw = 1, marker="o", markersize=3)  
    plt.ylim(bottom = 0)
    plt.show()

def graphInit():
    pass
def graphUpdate():
    line
def saveDB():
    pass;

main();