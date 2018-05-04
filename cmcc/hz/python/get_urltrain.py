from stations import stationsdic
import warnings

# f1= input('请输入起始城市：\n')
f1='杭州'
f = stationsdic[f1]

# t1= input('请输入目的城市：\n')
t1='南京'
t = stationsdic[t1]

# d1=input('请输入出发时间： \n')
d1='05-12'
d=str('2018-')+str(d1)   #2018-05-12      #这里讲年份设置为固定值，可以减少输入操作。
print ('正在查询'+f1+'至'+t1+'的列车，请稍等...')  #个性旁白

#url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+d+'&from_station='+f+'&to_station='+t

url ='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+d+'&leftTicketDTO.from_station='+f+'&leftTicketDTO.to_station='+t+'&purpose_codes=ADULT'
print(url)
warnings.filterwarnings("ignore")         #这个网站是有安全警告的，这段代码可以忽略警告</span></span>