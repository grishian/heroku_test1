import datetime
from myapp import db
from flask import abort
from myapp.bp_mushroom.model_mushroom import Mushroom

STAGE_SPAWN = 0
STAGE_FRUITING = 1
STAGE_HARVESTING = 2


class GrowRun(db.Model):
    __tablename__ = 'grow_run'

    id = db.Column('id', db.Integer, primary_key=True, index=True)
    mushroom_id = db.Column('mushroom_id', db.ForeignKey(Mushroom.id))
    mushroom_stage = db.Column('mushroom_stage', db.Integer, default=STAGE_SPAWN)
    grow_start = db.Column('grow_start', db.DateTime, default=datetime.datetime.now())
    spawn_start = db.Column('spawn_start', db.DateTime)
    fruit_start = db.Column('fruit_start', db.DateTime)
    active = db.Column('active', db.Boolean, default=True)

    temperatures = db.RelationshipProperty("Temperature", back_populates="grow_run")

    def __repr__(self):
        return '<GrowRun_id: {}, Mushroom_name: {}, GrowRun_start: {}>'.format(self.id,
                                                                               Mushroom.query.get(self.mushroom_id),
                                                                               self.grow_start)

    def get_mushroom(self): #not done!
        try:
            mushroom = Mushroom.query.get(self.mushroom_id)
        except Exception as e:
            abort(404)

        return mushroom

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True


def any_active():
    return bool(GrowRun.query.filter_by(active=1).first())
