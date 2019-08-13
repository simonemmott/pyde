from json_model import JsonModel

class ServerVariable(JsonModel):
    enum = JsonModel.list(str)
    default = JsonModel.field(str)
    description = JsonModel.field(str)


