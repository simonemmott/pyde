from json_model import JsonModel

class OAuthFlow(JsonModel):
    authorizationUrl = JsonModel.field(str)
    tokenUrl = JsonModel.field(str)
    refreshUrl = JsonModel.field(str)
    scopes = JsonModel.dict(str)


