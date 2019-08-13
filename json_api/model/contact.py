from json_model import JsonModel

class Contact(JsonModel):
    name = JsonModel.field(str)
    url = JsonModel.field(str)
    email = JsonModel.field(str)


