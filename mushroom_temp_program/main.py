from database import session
from datetime import datetime
from temp_upload import read_temp, GPIO

# check if there is a grown run active
# model grow run
# orrr good old queries?

# send temp to database
# database
# sqlalchemy, mariadb
# model temp
# orrr good old queries?


# testing connection
results = session.execute("SELECT COUNT(id) FROM grow_run WHERE active = 1")
active_grow_run_id = session.execute("SELECT id FROM grow_run WHERE active = 1").first()[0]
# get mushroom id
mushroom_id = session.execute("SELECT mushroom_id FROM grow_run WHERE active = 1").first()[0]

# check if mushroom is in spawn or in fruiting
if session.execute("SELECT spawn_start FROM grow_run WHERE active = 1").first()[0] is not None:
    # get mushroom spawn temp
    obtain_this_temperature = session.execute("SELECT spawn_temp FROM mushroom WHERE id = {}".format(mushroom_id)).first()[0]
if session.execute("SELECT fruit_start FROM grow_run WHERE active = 1").first()[0] is not None:
    # get mushroom fruit temp
    obtain_this_temperature = session.execute("SELECT fruit_temp FROM mushroom WHERE id = {}".format(mushroom_id)).first()[0]

temp_celsius = read_temp()
add_temperature = session.execute(
    "INSERT INTO temperature (grow_run_id, celsius, created_on) VALUES ('{}','{}','{}')".format(
        active_grow_run_id, temp_celsius, datetime.now()))

for result in results:
    if int(result[0]) == 1:
        print('one grow run active with id: {}'.format(active_grow_run_id))
        # insert temp to database

        print(add_temperature)
        session.commit()
        print('temperature added. ({} °C)'.format(temp_celsius))

        if temp_celsius < int(obtain_this_temperature):
            print('Temperature < {}'.format(obtain_this_temperature))
            print('Heatmat on.')
            GPIO.output(21, GPIO.HIGH)
        if temp_celsius >= int(obtain_this_temperature):
            print('Temperature >= {}'.format(obtain_this_temperature))
            print('Heatmat off.')
            GPIO.output(21, GPIO.LOW)



    else:
        print('No grow run is active or multiple grow runs are active.')
