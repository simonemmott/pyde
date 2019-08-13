from json_model import JsonModel
from .encoding import Encoding

class MediaType(JsonModel):
    schema = JsonModel.field('json_api.model.Schema')
    encoding = JsonModel.dict(Encoding)


