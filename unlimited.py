import requests
import pandas as pd
import json
import time
import math

'''
1、改成输入省市名城市名等，就可以出来所有的区县
2、做一个tk，让大家自备
'''


ad = input("请输入需要爬取的城市名称：")

if ad == "上海市":
    arr=['310101','310104','310105','310106''310107','310109','310110','310112','310113','310114','310115','310116','310117','310118','310120','310151']

elif ad == "北京市":
    arr=['110101','110102','110105','110106','110107','110108','110109','110111','110112','110113','110114','110115','110116','110117','110118','110119']

key_word = input("请输入需要爬取的关键词：")
key_='5173b1944e1f5032a3ac51379b051f37'
#input("请输入高德地图控制台key密钥（数据量大时需申请多个密钥）：")

url1="https://restapi.amap.com/v3/place/text?keywords="+str(key_word)+"&city="
url2="&output=JSON&offset=20&key="+str(key_)+"&extensions=all&page="
x=[['Name','Bigtype','Midtype','Lastype','address','lon','lat','tel','pname','cityname','adname']]
num=0
for i in range(0,len(arr)):
    #当前行政区
    city=arr[i]
    #因为官方对API检索进行了45页限制，所以只要检索到45页即可
    for page in range(1,46):
        #若该下级行政区的POI数量达到了限制，则警告使用者，之后考虑进行POI类型切分
        if page==45:
            print("警告！！POI检索可能受到限制！！")
        #构造URL
        thisUrl=url1+city+url2+str(page)
        #获取POI数据
        data=requests.get(thisUrl)
        #转为JSON格式
        s=data.json()
        #解析JSON
        aa=s["pois"]
        #若解析的JSON为空，即当前行政区的数据不够45页（即没有达到限制），返回
        if len(aa)==0:
            break
        #对每条POI进行存储
        for k in range(0,len(aa)):
                s1=aa[k]["name"]
                s2=aa[k]["type"].split(";")
                s3=aa[k]["address"]
                s4=aa[k]["location"].split(",")
                s5=aa[k]["tel"]
                s6=aa[k]["pname"]
                s7=aa[k]["cityname"]
                s8=aa[k]["adname"]
                x.append([s1,s2[0],s2[1],s2[2],s3,float(s4[0]),float(s4[1]),s5,s6,s7,s8])
                num+=1
                print("爬取了 "+str(num)+" 条数据")
 
c = pd.DataFrame(x)
#可更换存储路径
c.to_csv('h:/VScode/py/data_liujiao/poi/'+str(key_word)+'('+str(ad)+')'+'.csv',encoding='utf-8-sig')

print(str(key_word)+'('+str(ad)+')'+'数据爬取完毕！')
print('10秒后，将关闭此窗口！')
time.sleep(10)
