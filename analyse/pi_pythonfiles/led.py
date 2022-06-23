import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.cleanup


keuze = int(input('Wat is je keuze?'))

if keuze == 1:
    GPIO.cleanup
    print('LED on')
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print('LED off')
    GPIO.output(18,GPIO.LOW)
    GPIO.cleanup
    
if keuze == 2:
    counter = 1
    while True:
        GPIO.cleanup
        print('loop: {}'.format(counter))
        print('LED on')
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
        print('LED off')
        GPIO.output(18,GPIO.LOW)
        time.sleep(1)
        counter = counter + 1

if keuze == 3:
    GPIO.cleanup
    print('LED off')
    GPIO.output(18,GPIO.LOW)

