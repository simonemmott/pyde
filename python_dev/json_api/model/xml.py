from json_model import JsonModel

class Xml(JsonModel):
    name = JsonModel.field(str)
    namespace = JsonModel.field(str)
    prefix = JsonModel.field(str)
    attribute = JsonModel.field(bool)
    wrapped = JsonModel.field(bool)


