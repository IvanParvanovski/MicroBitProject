import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

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
    plt.plot(databaseAQ["DateTime"].tail(pointAmount),databaseAQ["Air Quality"].tail(pointAmount))
    plt.ylim(bottom = 0)
    plt.show()

def saveDB():
    pass;

main();