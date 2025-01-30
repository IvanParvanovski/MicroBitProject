import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt 

def main():
    global databaseAQ
    databaseAQ = initDB()
    pd.set_option('display.max_rows', 100) 
    pd.set_option('display.max_columns', 100) 
    show_DB()
    displayStaticGraphs()

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

def displayStaticGraphs():
    lineGraph()
    pieGraph()
    boxPlot()

def lineGraph():
    plt.title("Air Quality over time")
    plt.xlabel("TimeStamp")
    plt.ylabel("Air Quality")
    plt.grid(True)
    offset = 2
    plt.xlim(min(databaseAQ["TimeStamp"]) - offset, max(databaseAQ["TimeStamp"])+ offset)  
    plt.ylim(min(databaseAQ["Air Quality"])- offset, max(databaseAQ["Air Quality"])+ offset) 

    plt.plot(databaseAQ["TimeStamp"],databaseAQ["Air Quality"])

    databaseAQ["moving_average1"] = databaseAQ["Air Quality"].rolling(window=3).mean()
    plt.plot(databaseAQ["TimeStamp"], databaseAQ["moving_average1"], label='Moving Average (3 step)', color='red')

    databaseAQ["moving_average2"] = databaseAQ["Air Quality"].rolling(window=6).mean()
    plt.plot(databaseAQ["TimeStamp"], databaseAQ["moving_average2"], label='Moving Average (6 step)', color='green')

    databaseAQ["moving_average3"] = databaseAQ["Air Quality"].rolling(window=9).mean()
    plt.plot(databaseAQ["TimeStamp"], databaseAQ["moving_average3"], label='Moving Average (9 step)', color='purple')

    mean = round(databaseAQ["Air Quality"].mean(),2)
    plt.axhline(databaseAQ["Air Quality"].mean(),color='red', linestyle='--', linewidth=2, label=f'mean = {mean}')
    plt.legend()
    plt.show()

def pieGraph():
    sectorDict = {"Good" : 0,"Moderate" : 0,"Unhealthy (sensitive)" : 0,"Unhealthy" : 0,"Very Unhealthy" : 0,"Hazardous" : 0}
    for data in databaseAQ["Air Quality"]:
        if(data <= 50):
            sectorDict["Good"] += 1
        elif(data <= 100):
            sectorDict["Moderate"] += 1
        elif(data <= 150):
            sectorDict["Unhealthy (sensitive)"] += 1
        elif(data <= 200):
            sectorDict["Unhealthy"] += 1
        elif(data <= 300):
            sectorDict["Very Unhealthy"] += 1
        else:
            sectorDict["Hazardous"] += 1
    plt.title("Air Quality Assessment")
    plt.pie(sectorDict.values(), labels=sectorDict.keys(),autopct='%1.1f%%',startangle=90)
    plt.show()

def boxPlot():
    plt.boxplot(databaseAQ["Air Quality"])
    plt.ylabel("Air Quality")
    plt.title("Air Quality Distribution")
    plt.show()
main()