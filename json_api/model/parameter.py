from json_model import JsonModel
from .schema import Schema
from .media_type import MediaType
from .reference import Reference

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
    content = JsonModel.dict(MediaType)


