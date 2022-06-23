from myapp import db


class Mushroom(db.Model):
    __tablename__ = 'mushroom'

    id = db.Column('id', db.Integer, primary_key=True, index=True)
    name = db.Column('name', db.String(100), nullable=False)
    spawn_temperature = db.Column('spawn_temp', db.Integer, default=20)
    fruit_temperature = db.Column('fruit_temp', db.Integer, default=20)
    spawn_fae = db.Column('spawn_fae', db.Integer, default=5)
    fruit_fae = db.Column('fruit_fae', db.Integer, default=5)
    mushroom_img = db.Column('mushroom_img', db.String(300), default='https://images.unsplash.com/photo-1571074635691-b910c7a5cdbb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1203&q=80')

    notes = db.RelationshipProperty("Note", back_populates="mushroom")

    def __repr__(self):
        return '<Mushroom_name: {}, Mushroom_id: {}>'.format(self.name, self.id)


class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column('id', db.Integer, primary_key=True, index=True)
    mushroom_id = db.Column('mushroom_id', db.ForeignKey(Mushroom.id))
    title = db.Column('title', db.String(100), nullable=False)
    body = db.Column('body', db.TEXT(1000), nullable=False)

    mushroom = db.RelationshipProperty(Mushroom, foreign_keys='Note.mushroom_id', back_populates='notes')

    def __repr__(self):
        return '<Note_id: {}, Mushroom_name: {}, Note_title: {}, Note_body: {}...>'.format(self.id,
                                                                                           Mushroom.query.get(
                                                                                               self.mushroom_id).name,
                                                                                           self.title,
                                                                                           self.body[0:10])
