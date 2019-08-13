from json_model import JsonModel
from .o_auth_flows import OAuthFlows

class SecurityScheme(JsonModel):
    type = JsonModel.field(str, required=True)
    description = JsonModel.field(str)
    name = JsonModel.field(str)
    _in = JsonModel.field(str, alias='in')
    scheme = JsonModel.field(str)
    bearerFormat = JsonModel.field(str)
    flows = JsonModel.field(OAuthFlows)
    openIdConnectUrl = JsonModel.field(str)


