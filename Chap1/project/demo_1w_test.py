import time

def weather_dict_change():
    with open("weather_info.txt") as f:
        weather_dict = {}
        line = f.readline()
        print(line)
        print(line.split(",")[0])
        print(line.strip('\n'))
        print(line.strip('\n').split(",")[0])
        print(line.strip('\n')[0])
        print(line.split(",").strip('\n')[0])  

def weather_dict_change1():
    with open("weather_info.txt") as f:
        weather_dict = {}
        #line = f.readline()
        #print(line)
        #print(line.split(",")[0])
        #print(line.strip('\n'))
        #print(line.strip('\n').split(",")[0])
        #print(line.strip('\n')[0])
        ##print(line.split(",").strip('\n')[0])i  
        t1 = time.clock()
        lis = [list(x.strip('\n').split(",")) for x in list(f)]
        weather_dict = dict(lis) 
        t2= time.clock()
        print(t2-t1)
       # print(weather_dict)

def weather_dict_change2():
    with open("weather_info_test.txt") as f:
        weather_dict = {}
        for line in f:
            data_list = line.split(',')
            city = data_list[0]
            weather = data_list[1]
            weather_dict[city] = weather

        print(weather_dict)


weather_dict_change2()
