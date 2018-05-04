import json
from get_urltrain import d
import urllib
from urllib import request
import requests
from pprint import pprint
from get_urltrain import url
from prettytable import PrettyTable
from color_set import colored

#r = requests.get(url, verify=False)
print(url)
r = requests.get(url)
print(r)  #200
d=json.dumps(r.json())
print(d)
result0=(json.loads(d)['data']['result'])

print(len(result0)); #127
for row in result0:        # 第二个实例
    print(row.split('|'))

trains= PrettyTable()
trains.field_names=["车次","车站","时间","历时","商务座","特等座","一等座","二等座","高级软卧","软卧","硬卧 ","软座 ","硬座","无座"]
num = len(result0)
for result in result0 :
    row=result.split('|');
    trains.add_row([row[3],
                    '\n'.join([colored('green', row[6]),
                               colored('red', row[8])]),
                    '\n'.join([colored('green', row[7]),
                               colored('red', row[9])]),
                    row[10],row[32],row[32],row[31],
                    row[30],row[21],row[23],
                    row[28],row[24],row[29],
                    row[26]])
print ('查询结束，共有 %d 趟列车。'%num )
print (trains)