from flask import Flask, render_template
import pandas as pd
import numpy as np
import glob
import json
from datetime import datetime
import calendar, time
 
app = Flask(__name__)

@app.route('/')
@app.route('/graph')
def graph():
    chartInfo = graphs()
    return render_template('index.html', chartInfo=chartInfo)

@app.route('/temperature')
def temperature():
 chartInfo = graphs()
 return render_template('temperature.html', chartInfo=chartInfo)

@app.route('/ph')
def ph():
 chartInfo = graphs()
 return render_template('ph.html', chartInfo=chartInfo)

@app.route('/do')
def do():
 chartInfo = graphs()
 return render_template('do.html', chartInfo=chartInfo)



def graphs():
    files = glob.glob("csv/table.csv")
    df = pd.read_csv(files[0])

    renderTo = ['DO','TEMPERATURE','PH']
    option =['do','temperature','ph']
    ttext=['용존 산소량','수온', '수소 이온 농도']
    ytext=['DO','TEMPERATURE','PH']
    chartInfo = []
    chart_type = 'line'
    chart_height = 500
    for i in range(3):
        chart = {"renderTo": renderTo[i], "type": chart_type, "height": chart_height}
        series = getSeries(df,option[i])
        title = {"text":ttext[i]}
        xAxis = {"type":"datetime", 'lineWidth':3,"dateTimeLabelFormats": {
            "minute": '%m월 %d일'
        },
        "startOnTick": 'true',
        "endOnTick": 'true',
        "showLastLabel": 'true',
        "labels": {
            "rotation": 0,
            "style":{
                "fontSize":8
            }
        },}
        yAxis = {"title":{"text":ytext[i]},"min":0, "max":20, 'lineWidth':1, 
                 "labels": {
                    "rotation": 0,
                    "style":{
                        "fontSize":10
                     }
                }
                 
                 }
        
        chartInfo.append([chart, series, title, xAxis, yAxis])

    return chartInfo

def getSeries(df,option):
    #수조 탱크의 구분을 위한 프로세스
    tank_type = df.tank_id.unique()
    series = '['
    for i in range(len(tank_type)):
        #수조 탱크는 현재 1,2 가 끝
        tank = tank_type[i]
        series += '{"name" : "Tank-' + str(tank) + '", "data" : ['
        for index, row in df.iterrows():
            if row['tank_id'] == tank and index % 4 == 0:
                #print(row['date'])
                #print(int(datetime.strptime(row['date'], '%Y-%M-%d').timestamp()))
                #print('\n')
                series += '[' + str(calendar.timegm(time.strptime(row['date'], '%Y-%m-%d'))) + ',' + str(int(row[option])) + '],'                   
        series = series[:-1]
        series += ']},'
       
    series = series[:-1] + ']'
    print(series)
    return series
 
if __name__ == "__main__":  
    app.run(debug = True, host='0.0.0.0', port=5000, passthrough_errors=True)
