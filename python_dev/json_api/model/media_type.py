from json_model import JsonModel, Any
from .encoding import Encoding
from .example import Example

class MediaType(JsonModel):
    schema = JsonModel.field('Schema')
    example = JsonModel.field(Any)
    examples = JsonModel.list(Example)
    encoding = JsonModel.dict(Encoding)


