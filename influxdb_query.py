#!/usr/bin/env python
#coding:UTF-8
from influxdb import client as influxdb
import pandas as pd
import datetime

host = 'api-beta.ly.g0v.tw'
port = '8086'
username = 'guest'
password = 'guest'
database = 'twer'
db = influxdb.InfluxDBClient(host, port, username, password, database)

result = db.query('select last(pending_ward) as ward, DIFFERENCE(pending_ward) as ward_diff  from ER group by hospital_sn, time(1h) where time > now() - 24h')

# result returns to a list; result[0] returns to dict 
# result[0]['columns'] provides column name
# result[0]['points'] provides the list data
#data = pd.DataFrame(A, columns=col_name)
#print result[0]['columns'][0]

data = pd.DataFrame(result[0]['points'], columns=result[0]['columns'])  # 把 sql query 回來的讀進 dataframe
table = pd.tools.pivot.pivot_table(data, index=['time'], columns=['hospital_sn'])  # 把 hospital_sn 拉到 columns
print table.plot()   


A = data.ix[data['hospital_sn'] == '0401180014']   # 指定某SN
A['time'] = [datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S') for x in A['time']]  # 把 timestamp 轉成 datatime
print A.plot(x='time', y='ward')   # plot 指定一個column 當X , 另一個當Y


