#coding:utf-8

import time
from bluetooth import *

#get time now
hour = int(time.asctime()[-13:-11])
print('this time:',hour)
#scan the bluetooth in 9-11
while(hour >= 9 and hour <= 11):
    devList = discover_devices()
    for device in devList:
        name = str(lookup_name(device))
        print('发现蓝牙设备: ' + str(name))
        print('MAC地址为: ' + str(device))
print('time out')