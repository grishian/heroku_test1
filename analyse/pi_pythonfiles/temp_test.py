#!/usr/bin/env python

# DS18B20 waterdichte temperatuur sensor aansluiten op Raspberry Pi
# https://raspberrytips.nl/ds18b20-raspberry-pi/

import os
import glob
import time

import RPi.GPIO as GPIO
import time


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT) #changing this from 18 to 2 because this gio pin is 5V output
GPIO.cleanup


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

while True:
        temp_c = read_temp()
        print(read_temp())
        if temp_c < 21:
            print('Heatmat on')
            GPIO.output(2, GPIO.HIGH)
        time.sleep(1)
        if temp_c >= 21:
            print('Heatmat off')
            GPIO.output(2, GPIO.LOW)
        
        
        
        
        
        
        
        