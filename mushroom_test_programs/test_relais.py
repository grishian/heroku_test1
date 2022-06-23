import os
import glob
import RPi.GPIO as GPIO
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.cleanup


while True:
    time.sleep(1)
    print('Heatmat on.')
    GPIO.output(21, GPIO.HIGH)
    time.sleep(1)
    print('Heatmat off.')
    GPIO.output(21, GPIO.LOW)





