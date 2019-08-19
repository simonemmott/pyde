from json_model import JsonModel, Any
from .schema import Schema
from .media_type import MediaType
from .reference import Reference
from .example import Example

class Parameter(JsonModel):
    name = JsonModel.field(str, required=True)
    _in = JsonModel.field(str, alias='in', required=True, choices=['query', 'header', 'path', 'cookie'])
    description = JsonModel.field(str)
    required = JsonModel.field(bool)
    deprecated = JsonModel.field(bool)
    allowEmptyValue = JsonModel.field(bool)
    style = JsonModel.field(str)
    explode = JsonModel.field(bool)
    allowReserved = JsonModel.field(bool)
    schema = JsonModel.field(Schema)
    example = JsonModel.field(Any)
    examples = JsonModel.dict(Example)
    content = JsonModel.dict(MediaType)


