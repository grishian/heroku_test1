import datetime

from myapp import db
from myapp.bp_grow_run.model_grow_run import GrowRun


class Temperature(db.Model):
    __tablename__ = 'temperature'

    id = db.Column('id', db.Integer, primary_key=True, index=True)
    celsius = db.Column('celsius', db.Integer)
    grow_run_id = db.Column('grow_run_id', db.ForeignKey(GrowRun.id), nullable=False, index=True)
    created_on = db.Column('created_on', db.DateTime, default=datetime.datetime.now())

    grow_run = db.RelationshipProperty(GrowRun, foreign_keys='Temperature.grow_run_id', back_populates='temperatures')

    def __repr__(self):
        return '<Temperature_id: {}, celsius: {}, grow_run_id: {}>'.format(self.id, self.celsius, self.grow_run_id)

