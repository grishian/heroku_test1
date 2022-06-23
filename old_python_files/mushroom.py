from utils import print_title
from inputs import get_input_item
from database import BaseObject, session
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship


FIRST_STATE = 'SPAWN'
SECOND_STATE = 'FRUITING'

class Mushroom(BaseObject):
    __tablename__ = 'T_MUSHROOM'

    name = Column('F_NAME', String(100), nullable=False)
    spawn_temperature = Column('F_SPAWN_TEMP', Integer, default=20)
    fruit_temperature = Column('F_FRUIT_TEMP', Integer, default=20)
    spawn_fae = Column('F_SPAWN_FAE', Integer, default=5)
    fruit_fae = Column('F_FRUIT_FAE', Integer, default=5)

    #grow_runs = relationship("GrowRun", back_populates="mushroom") no idea what to do here


    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


def add_mushroom(mushroom = None):
    if mushroom is None:
        print_title('Add new mushroom:')
        m = Mushroom()
    else:
        m = mushroom

    m.name = get_input_item('Give mushroom name: ')
    m.spawn_temperature = get_input_item('Give spawn temperature: ', 1)
    m.fruit_temperature = get_input_item('Give fruiting temperature: ', 1)
    m.spawn_fae = get_input_item('Give frequently air exchange for spawn: ', 1)
    m.fruit_fae = get_input_item('Give frequently air exchange for fruiting: ', 1)

    session.add(m)
    session.commit()


def search_mushroom():
    inp = get_input_item('Search mushroom by name (empty to show all): ')

    qry = session.query(Mushroom)
    if inp != '':
        inp = '%{}%'.format(inp)
        qry = qry.filter(Mushroom.name.like(inp))

    mushrooms = qry.order_by(Mushroom.name).all()

    for mushroom in mushrooms:
        print(mushroom)


