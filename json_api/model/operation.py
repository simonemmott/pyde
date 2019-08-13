from json_model import JsonModel
from .external_docs import ExternalDocs
from .parameter import Parameter
from .request_body import RequestBody
from .response import Response
from .callback import Callback
from .security_requirement import SecurityRequirement
from .server import Server
from .reference import Reference

class Operation(JsonModel):
    tags = JsonModel.list(str)
    summary = JsonModel.field(str)
    description = JsonModel.field(str)
    externalDocs = JsonModel.field(ExternalDocs)
    operationid = JsonModel.field(str)
    parameters = JsonModel.list(Parameter)
    requestBody = JsonModel.field(RequestBody)
    responses = JsonModel.dict(Response, required=True)
    callbacks = JsonModel.dict(Callback, required=True)
    deprecated = JsonModel.field(bool)
    security = JsonModel.list(SecurityRequirement)
    servers = JsonModel.list(Server)


