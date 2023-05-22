from ... import db
from ...models.section import Section
from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal

section_fields = {
    'id': fields.Integer,
    'heading': fields.String,
    'parent_section': fields.String,
    'book_id':fields.Integer,
}

class SectionResource(Resource):
    def get(self,book_id=None,section_id=None):
        if section_id:
            return  marshal(Section.query.filter_by(book_id=book_id,id=section_id).all(), section_fields)        
        return  marshal(Section.query.filter_by(book_id=book_id).all(),section_fields)
    
