import datetime
from utils import print_title
from inputs import get_input_item
from database import BaseObject, session
from sqlalchemy import ForeignKey, Column, String, DateTime
from sqlalchemy.orm import relationship
from mushroom import Mushroom


class GrowRun(BaseObject): # misschien grow_box noemen?

    __tablename__ = 'T_GROW_RUN'

    name = Column('F_NAME', String(100), nullable=False)
    mushroom_id = Column('F_MUSHROOM_ID', ForeignKey(Mushroom.id))
    mushroom_stage = Column('F_MUSHROOM_STAGE', String(15), default='fruiting')
    grow_start = Column('F_GROW_START', DateTime, default=datetime.datetime.now())
    spawn_start = Column('F_SPAWN_START', DateTime)
    fruit_start = Column('F_FRUIT_START', DateTime)
    is_active = Column('F_IS_ACTIVE', String(15), nullable=False, default='not_active')

    temperatures = relationship("Temperature", back_populates="grow_run")
    #mushroom = relationship(Mushroom, foreign_keys='GrowRun.mushroom_id', back_populates="grow_runs")

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


def add_grow_run(grow_run = None):
    previous_id = session.query(GrowRun).count()
    last_grow_run = session.query(GrowRun).get(previous_id)
    last_grow_run.is_active = 'not_active'

    if grow_run is None:
        print_title('Add new grow run:')
        g = GrowRun()
    else:
        g = grow_run

    g.name = get_input_item('Give grow name: ')
    print_title('Available mushrooms: ')

    mushrooms = session.query(Mushroom).order_by(Mushroom.id).all()

    for mushroom in mushrooms:
        print(mushroom)

    g.mushroom_id = get_input_item('Give mushroom id: ', 1)
    g.mushroom_stage = get_input_item('Give mushroom stage: ')
    g.is_active = 'active'

    session.add(g)
    session.commit()






