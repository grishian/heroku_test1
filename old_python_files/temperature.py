from utils import print_title
from inputs import get_input_item
from sqlalchemy import ForeignKey, Column, Integer
from database import BaseObject, session
from sqlalchemy.orm import relationship
from grow_run import GrowRun


class Temperature(BaseObject):
    __tablename__ = 'T_TEMPERATURE'

    celsius = Column('F_CELSIUS', Integer, default=20)
    grow_run_id = Column('F_GROW_RUN_ID', ForeignKey(GrowRun.id), nullable=False, index=True)

    grow_run = relationship(GrowRun, foreign_keys='Temperature.grow_run_id', back_populates="temperatures")

    def __str__(self):
        return 'id:{}: {} degree celsius'.format(self.id, self.celsius)


def add_temp(temp = None):

    '''look into database table growruns
    look for grow runs with is_active: active only one grow run can be active for now
    create new Temperature
    take growrun id and tempsensor celsius
    add, commit to session
    '''


    if temp is None:
        print_title('Add new temperature:')
        t = Temperature()
    else:
        t = temp

    t.grow_run_id = get_input_item('Give grow run id: ', 1)
    t.celsius = get_input_item('Give a temperature in celsius: ', 1)

    session.add(t)
    session.commit()

'''
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
    GPIO.setup(18, GPIO.OUT)
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
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

    while True:
        temp_c = read_temp()
        t = Temperature()
        t.celsius = temp_c
        #make grow run attribute: is_active
        t.grow_run_id = 1

        session.add(t)
        session.commit()
        time.sleep(12)

        
'''


def search_temperatures():
    latest_growrun_id = session.query(GrowRun).count()

    qry = session.query(Temperature)
    qry = qry.filter(Temperature.grow_run_id.like(latest_growrun_id))
    temperatures = qry.order_by(Temperature.id).all()

    print('{} temperatures found:'.format(len(temperatures)))

    for temperature in temperatures:
        print(temperature)

def search_average_temperature():
    latest_growrun_id = session.query(GrowRun).count()

    qry = session.query(Temperature)
    qry = qry.filter(Temperature.grow_run_id.like(latest_growrun_id))
    temperatures = qry.order_by(Temperature.id).all()

    sum_temp = 0
    for temperature in temperatures:
        sum_temp = sum_temp + temperature.celsius

    average_temp = sum_temp/len(temperatures)

    print('\nThe average temperature is: {} degree celsius.'.format(average_temp))

def search_min_temperature():
    latest_growrun_id = session.query(GrowRun).count()

    qry = session.query(Temperature)
    qry = qry.filter(Temperature.grow_run_id.like(latest_growrun_id))
    temperatures = qry.order_by(Temperature.id).all()

    temperatures_celsius = []

    for temperature in temperatures:
        temperatures_celsius.append(temperature.celsius)

    min_temperature = min(temperatures_celsius)

    print('\nThe minimum temperature is: {} degree celsius.'.format(min_temperature))


def search_max_temperature():
    latest_growrun_id = session.query(GrowRun).count()

    qry = session.query(Temperature)
    qry = qry.filter(Temperature.grow_run_id.like(latest_growrun_id))
    temperatures = qry.order_by(Temperature.id).all()

    temperatures_celsius = []

    for temperature in temperatures:
        temperatures_celsius.append(temperature.celsius)

    max_temperature = max(temperatures_celsius)

    print('\nThe maximum temperature is: {} degree celsius.'.format(max_temperature))

