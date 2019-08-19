from json_model import JsonModel
from .contact import Contact
from .license import License

class Info(JsonModel):
    title = JsonModel.field(str, required=True)
    description = JsonModel.field(str)
    termsOfService = JsonModel.field(str)
    contact = JsonModel.field(Contact)
    license = JsonModel.field(License)
    version = JsonModel.field(str, required=True)


