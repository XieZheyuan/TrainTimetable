import requests
# from urllib import parse
import prettytable
import re
import colorama
def real(l):
    for i in l:
        if(i != ''):
            return i
    return -1

code=input("输入班次：\n")
url="http://qq.ip138.com/train/%s.htm"%code

data=requests.get(url)
encode=data.encoding
# print(encode)
if(data.status_code == 404):
    print("没有查到：%s"%code)
    exit(1)
data=data.content.decode("gb2312")

title=re.search("<h1>.*</h1>",data).group(0)
title=title.replace("<h1>","")
title=title.replace("</h1>","")
start=re.search("从.*开往",title).group(0).replace("从","")\
    .replace("开往","")
end=re.search("往.*%s"%code.lower(),title).group(0).replace("往","").replace(code.lower(),"")
train_type=re.search("列车类型：.*&nbsp;",data).group(0).replace("&nbsp;","").replace("</td>","").replace("<td>","")
print(title)
print()
print(colorama.Style.BRIGHT+"从%s开往%s"%(start,end)+
      colorama.Style.RESET_ALL)
print(train_type)
train_station=re.findall("<a href=\"/train.*\" target=\"_blank\">.*</a>",data)
# print("-"*100)
train_time=re.findall("([0-9]{2}:[0-9]{2})|(---)",data)
train_time.pop(0)
# print(train_time)
print("")
tableHead=["车站","到达时间","发车时间","走行时间（小时）"]
for i in tableHead:
    tableHead[tableHead.index(i)]=colorama.Fore.GREEN+i+colorama.Fore.RESET
tableObj=prettytable.PrettyTable(tableHead)
tableObj.header=True
tableObj.horizontal_char = '-'
tableObj.junction_char='|'
cnt=0
for i in train_station:
    row=[]
    j=i.replace("</a>","")

    e=j.index(">")

    # print(j[e+1:],
    #       real(train_time[cnt]),
    #       real(train_time[cnt+1]),
    #       real(train_time[cnt+2]))
    row.append(colorama.Fore.RED+j[e+1:]+colorama.Fore.RESET)
    # print(colorama.Back.BLACK)
    row.append(colorama.Fore.LIGHTMAGENTA_EX+real(train_time[cnt]))
    row.append(real(train_time[cnt+1]))
    row.append(real(train_time[cnt+2]))
    print(colorama.Fore.RESET)
    tableObj.add_row(row)
    cnt=cnt+3
# print(colorama.Back.BLACK)
print(tableObj)
# print(colorama.Back.RESET)
