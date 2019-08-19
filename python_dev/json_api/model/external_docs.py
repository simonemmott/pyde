from json_model import JsonModel

class ExternalDocs(JsonModel):
    description = JsonModel.field(str)
    url = JsonModel.field(str, required=True)


