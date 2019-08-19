from json_model import JsonModel

class License(JsonModel):
    name = JsonModel.field(str)
    url = JsonModel.field(str)


