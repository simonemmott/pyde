from json_model import JsonModel, Any

class Example(JsonModel):
    summary = JsonModel.field(str)
    description = JsonModel.field(str)
    value = JsonModel.field(Any)
    externalValue = JsonModel.field(str)


