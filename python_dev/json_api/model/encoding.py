from json_model import JsonModel
from .header import Header

class Encoding(JsonModel):
    contentType = JsonModel.field(str)
    headers = JsonModel.dict(Header)
    style = JsonModel.field(str)
    explode = JsonModel.field(bool)
    allowReserved = JsonModel.field(bool)
    
    


