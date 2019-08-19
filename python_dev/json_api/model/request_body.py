from json_model import JsonModel
from .media_type import MediaType

class RequestBody(JsonModel):
    description = JsonModel.field(str)
    content = JsonModel.dict(MediaType, required=True)
    required = JsonModel.field(bool)


