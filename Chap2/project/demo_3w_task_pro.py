from apixu.client import ApixuClient, ApixuException
api_key = 'bc640bce45574adfbe235846172308'
client = ApixuClient(api_key)

def main():

    while True:
        cmd = input("请输入命令或要查询城市名，注意国内城市请输入拼音，国外城市输入英文:")
        day  = int(input("请问要查询几天后的天气:"))
        forecast = client.getForecastWeather(q=cmd, days=10)
        if cmd in ["quit"]:
            print("程序退出")
            break
        elif "error" in forecast:
            print('输入的城市无效或命令无效')
        else: 
            print ("要查询的日期:",forecast['forecast']['forecastday'][day]['date']) 
            print ("平均气温:",forecast['forecast']['forecastday'][day]['day']['avgtemp_c']) 
            print ("天气状态:",forecast['forecast']['forecastday'][day]['day']['condition']['text']) 

if __name__ == '__main__':
    main()



# "forecast" is a dict with a structure like this:
'''
{
    'current': {
        ...
    },
    'location': {
        ...
    },
    'forecast': {
        'forecastday': [{
            'astro': {
                'moonrise': '06:07 PM',
                'moonset': '03:33 AM',
                'sunrise': '05:29 AM',
                'sunset': '08:32 PM'
            },
            'date': '2015-06-29',
            'date_epoch': 1435536000,
            'day': {
                'avgtemp_c': 21.7,
                'avgtemp_f': 71.1,
                'condition': {
                    'code': 1063,
                    'icon': 'http://www.apixu.com/static/weather/64x64/day/176.png',
                    'text': 'Patchy rain nearby'
                },
                'maxtemp_c': 27.6,
                'maxtemp_f': 81.7,
                'maxwind_kph': 25.2,
                'maxwind_mph': 15.7,
                'mintemp_c': 17.5,
                'mintemp_f': 63.5,
                'totalprecip_in': 0.01,
                'totalprecip_mm': 0.2
            },
            'hour': [{
                'cloud': 16,
                'condition': {
                    'code': 1000,
                    'icon': 'http://www.apixu.com/static/weather/64x64/night/113.png',
                    'text': 'Clear '
                },
                'dewpoint_c': 15.1,
                'dewpoint_f': 59.2,
                'feelslike_c': 18.4,
                'feelslike_f': 65.1,
                'heatindex_c': 18.4,
                'heatindex_f': 65.1,
                'humidity': 81,
                'precip_in': 0.0,
                'precip_mm': 0.0,
                'pressure_in': 30.2,
                'pressure_mb': 1007.0,
                'temp_c': 18.4,
                'temp_f': 65.1,
                'time': '2015-06-29 00:00',
                'time_epoch': 1435536000,
                'will_it_rain': 0,
                'will_it_snow': 0,
                'wind_degree': 255,
                'wind_dir': 'WSW',
                'wind_kph': 25.6,
                'wind_mph': 15.9,
                'windchill_c': 18.4,
                'windchill_f': 65.1
            }]
        }]
    },
}
'''

