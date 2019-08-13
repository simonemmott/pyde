from json_model import JsonModel
from .server_variable import ServerVariable

class Server(JsonModel):
    url = JsonModel.field(str)
    description = JsonModel.field(str)
    variables = JsonModel.dict(ServerVariable)


