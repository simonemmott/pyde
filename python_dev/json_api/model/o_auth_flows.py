from json_model import JsonModel
from .o_auth_flow import OAuthFlow

class OAuthFlows(JsonModel):
    implicit = JsonModel.field(OAuthFlow)
    password = JsonModel.field(OAuthFlow)
    clientCredentials = JsonModel.field(OAuthFlow)
    authorizationCode = JsonModel.field(OAuthFlow)
    


