from json_model import JsonModel
from .operation import Operation
from .server import Server
from .parameter import Parameter
from .reference import Reference

class PathItem(JsonModel):
    _ref = JsonModel.field(str, '$ref')
    summary = JsonModel.field(str)
    description = JsonModel.field(str)
    get = JsonModel.field(Operation)
    put = JsonModel.field(Operation)
    post = JsonModel.field(Operation)
    delete = JsonModel.field(Operation)
    options = JsonModel.field(Operation)
    head = JsonModel.field(Operation)
    patch = JsonModel.field(Operation)
    trace = JsonModel.field(Operation)
    servers = JsonModel.list(Server)
    parameters = JsonModel.list(Parameter)


