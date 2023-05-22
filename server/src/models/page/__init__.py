from ... import db

class Page(db.Model):

    __tablename__ = 'page'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    page_number = db.Column(db.Integer,nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'),nullable=False)
    
    def __repr__(self):
        return 'Id: {}, section_id: {}'.format(self.id, self.section_id)