from json_model import JsonModel
from .response import Response
from .parameter import Parameter
from .example import Example
from .request_body import RequestBody
from .header import Header
from .security_scheme import SecurityScheme
from .link import Link
from .callback import Callback
from .reference import Reference

class Components(JsonModel):
    schemas = JsonModel.dict('Schema')
    responses = JsonModel.dict(Response)
    parameters = JsonModel.dict(Parameter)
    examples = JsonModel.dict(Example)
    requestBodies = JsonModel.dict(RequestBody)
    headers = JsonModel.dict(Reference)
    securitySchemes = JsonModel.dict(SecurityScheme)
    links = JsonModel.dict(Link)
    callbacks = JsonModel.dict(Callback)


