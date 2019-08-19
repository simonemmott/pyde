from json_model import JsonModel

class Reference(JsonModel):
    _ref = JsonModel.field(str, '$ref')


