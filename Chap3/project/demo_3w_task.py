import requests
import json
from utils.const_value import API, KEY, UNIT, LANGUAGE
from utils.helper import getLocation

def fetchWeather(location):
    result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=1)

    return result.status_code,result.json()

def main():
    record = []
    while True:
        cmd = input("请输入城市名或指令:")
        status,result = fetchWeather(cmd)
        #print (status)
        if status == 200: 
            info = json.loads(result)
            now_text = info['results'][0]['now']['text']
            now_temperature = info['results'][0]['now']['temperature']
            last_update = info['results'][0]['last_update']
           # weather_p = u'更新时间:{},{}的天气状况是:{},温度:{}摄氏度'.format(last_update,cmd,now_text,now_temperature)
            print(weather_p)
            print("%s天气状况的天气状况为:%s,温度是:%s摄氏度"%(cmd,now_text,now_temperature))
            print("更新时间:%s"%(last_update))
            record.append([cmd,now_text,now_temperature,last_update])
        elif cmd in ["history","his"]:
                print(record)
        elif cmd in ["help","h"]:
            print("\n输入城市名，查询该城市的天气；\n")
            print("输入help，获取帮助文档；\n")
            print("输入history，获取查询历史；\n")
            print("输入quit，退出天气查询系统。\n")
        elif cmd in ["quit","q"]:
            print("程序退出")
            break
        else:
            print("输入命令无效")

if __name__ == '__main__':
    main()




