from json_model import JsonModel
from .external_docs import ExternalDocs

class Tag(JsonModel):
    name = JsonModel.field(str, required=True)
    description = JsonModel.field(str)
    externalDocs = JsonModel.field(ExternalDocs)


