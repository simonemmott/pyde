from json_model import JsonModel

class Discriminator(JsonModel):
    propertyName = JsonModel.field(str)
    mapping = JsonModel.dict(str)


