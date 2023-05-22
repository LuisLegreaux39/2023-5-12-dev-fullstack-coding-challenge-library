from ... import db
from ...models.book import Book
from ...models.section import Section
from flask_restful import Resource
from flask_restful import fields, marshal

book_fields = {
    'id': fields.Integer,
    'cover_image':fields.String,
    'name': fields.String,
    'description': fields.String,
}

class BookResource(Resource):
    def get(self,book_id=None):
        if book_id:   
            return marshal(
                Book.query.filter_by(id=book_id).first(),
                book_fields)
            
        return  marshal(
            Book.query.all(),
            book_fields)
