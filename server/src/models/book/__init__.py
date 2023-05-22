from ... import db

class Book(db.Model):

    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    cover_image = db.Column(db.String())
    name = db.Column(db.String(200))
    description = db.Column(db.String())
    
    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id, self.name)