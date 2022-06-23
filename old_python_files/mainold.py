from utils import print_title
from inputs import get_input_item
from database import create_database, delete_tables, session
from mushroom import add_mushroom, search_mushroom, Mushroom
from temperature import add_temp, search_temperatures, search_average_temperature, search_min_temperature, search_max_temperature
from grow_run import add_grow_run


def main_menu():
    print_title('Menu')
    options = {1: 'tables menu',
               2: 'mushroom menu',
               3: 'grow run menu'
               }

    for option in options:
        print('{}: {}'.format(option, options[option]))

    choice = get_input_item('What do you want to do? Give number: \n'
                            '(empty to exit)', 1)

    if choice == 1:
        print_title('Database menu:')
        db_menu()
    if choice == 2:
        print_title('Mushroom menu:')
        mushroom_menu()
    if choice == 3:
        print_title('Grow run menu:')
        grow_run_menu()

    print_title('Finished...')


def db_menu():
    '''
    menu that handles:
    - database:
        - add tables
        - delete tables

    '''


    options = {1: 'add tables',
               2: 'delete tables'
               }

    for option in options:
        print('{}: {}'.format(option, options[option]))

    choice = get_input_item('What do you want to do? Give number: \n'
                            '(empty to exit): ', 1)

    if choice == 1:
        print_title('Adding tables...')
        create_database()
    if choice == 2:
        print_title('Deleting tables...')
        delete_tables()

def mushroom_menu():
    '''
    menu that handles:
    - mushrooms:
        - add mushrooms
        - search mushrooms
    - possible update:
        - edit mushrooms
        - delete mushrooms

    '''

    options = {1: 'add mushroom',
               2: 'search mushroom'
               }

    for option in options:
        print('{}: {}'.format(option, options[option]))

    choice = get_input_item('What do you want to do? Give number: \n'
                            '(empty to exit): ', 1)

    if choice == 1:
        print_title('Adding mushroom...')
        add_mushroom()
    if choice == 2:
        print_title('Searching mushroom...')
        search_mushroom()


def grow_run_menu():
    '''
    menu that handles:
    - grow run
    - temperatures of certain grow run:
        - all temperatures
        - average temperature
        - max/min temperature

    '''


    options = {1: 'add grow run',
               2: 'search temperatures',
               3: 'add temperatures',
               4: 'search average temperature',
               5: 'search min temperature',
               6: 'search max temperature'
               }

    for option in options:
        print('{}: {}'.format(option, options[option]))

    choice = get_input_item('What do you want to do? Give number: \n'
                            '(empty to exit): ', 1)

    if choice == 1:
        #check if any mushrooms are available
        qry = session.query(Mushroom).count()
        if qry < 1:
            print_title('First add a mushroom please.')
            add_mushroom()
        else:
            print_title('Adding grow run...')
            add_grow_run()
            #add_temp() add_temps?
    if choice == 2:
        print_title('Searching temperatures...')
        search_temperatures()
    if choice == 3:
        print_title('Adding temperature...')
        add_temp()
    if choice == 4:
        print_title('Searching average temperature...')
        search_average_temperature()
    if choice == 5:
        print_title('Searching minimum temperature...')
        search_min_temperature()
    if choice == 6:
        print_title('Searching maximum temperature...')
        search_max_temperature()


def do_run():
    main_menu()


if __name__ == '__main__':
    do_run()
