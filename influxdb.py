from influxdb import client as influxdb

host = 'api-beta.ly.g0v.tw'
port = '8086'
username = 'guest'
password = 'guest'
database = 'twer'
db = influxdb.InfluxDBClient(host, port, username, password, database)

result = db.query('select last(pending_ward) as ward, DIFFERENCE(pending_ward) as ward_diff  from ER group by hospital_sn, time(1h) where time > now() - 24h')


result
