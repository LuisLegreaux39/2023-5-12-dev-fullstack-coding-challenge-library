from ... import db

class Section(db.Model):

    __tablename__ = 'section'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'),nullable=False)
    heading = db.Column(db.String(200))
    parent_section = db.Column(db.String(200))
    
    def __repr__(self):
        return 'Id: {}, book_id: {}'.format(self.id, self.heading)