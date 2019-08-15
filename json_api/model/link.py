from json_model import JsonModel, Any
from .server import Server

class Link(JsonModel):
    operationRef = JsonModel.field(str)
    operationid = JsonModel.field(str)
    parameters = JsonModel.dict(Any)
    requestBody = JsonModel.field(Any)
    description = JsonModel.field(str)
    server = JsonModel.field(Server)


