
from src.controller.book.resource import BookResource
from src.controller.section.resource import SectionResource
from src.controller.page.resource import PageResource

def set_routes(api):
    api.add_resource(
        BookResource, 
        "/book",
        "/book/<int:book_id>"
        )
    api.add_resource(
        SectionResource, 
        "/book/<int:book_id>/section",
        "/book/<int:book_id>/section/<int:section_id>"
        )
    api.add_resource(
        PageResource, 
        "/book/<int:book_id>/section/<int:section_id>/page",
        "/book/<int:book_id>/section/<int:section_id>/page/<int:page_number>"
        )
    return