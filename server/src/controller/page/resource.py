from ... import db
from ...models.page import Page
from flask_restful import Resource
from flask_restful import fields, marshal

page_fields = {
    'id': fields.Integer,
    'content': fields.String,
    'section_id': fields.Integer,
}

class PageResource(Resource):
    def get(self,book_id=None,section_id=None,page_number=None):
        if(section_id):
             return marshal(
                Page.query.filter_by(section_id=section_id).all(),
                page_fields
            )
        return marshal(
            Page.query.all(),
            page_fields
        )
