from influxdb import client as influxdb
import pandas as pd

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

data = pd.DataFrame(result[0]['points'], columns=result[0]['columns'])

print data
