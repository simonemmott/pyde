from json_model import JsonModel
from .server import Server

class Link(JsonModel):
    operationRef = JsonModel.field(str)
    operationid = JsonModel.field(str)
    parameters = JsonModel.dict(str)
    requestBody = JsonModel.field(str)
    description = JsonModel.field(str)
    server = JsonModel.field(Server)


