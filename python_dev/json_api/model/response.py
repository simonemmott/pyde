from json_model import JsonModel
from .header import Header
from .media_type import MediaType
from .link import Link

class Response(JsonModel):
    description = JsonModel.field(str, required=True)
    headers = JsonModel.dict(Header)
    content = JsonModel.dict(MediaType)
    links = JsonModel.dict(Link)

