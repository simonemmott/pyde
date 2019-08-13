from json_model import JsonModel

class Header(JsonModel):
    description = JsonModel.field(str)
    required = JsonModel.field(bool)
    deprecated = JsonModel.field(bool)
    allowEmptyValue = JsonModel.field(bool)
    style = JsonModel.field(str)
    explode = JsonModel.field(bool)
    allowReserved = JsonModel.field(bool)
    schema = JsonModel.field('json_api.model.Schema')
    content = JsonModel.dict('json_api.model.MediaType')


