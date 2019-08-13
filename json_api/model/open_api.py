from json_model import JsonModel
from .info import Info
from .server import Server
from .path_item import PathItem
from .components import Components
from .security_requirement import SecurityRequirement
from .tag import Tag
from .external_docs import ExternalDocs

class OpenApi(JsonModel):
    openapi = JsonModel.field(str, required=True)
    info = JsonModel.field(Info, required=True)
    servers = JsonModel.list(Server)
    paths = JsonModel.dict(PathItem, required=True)
    components = JsonModel.field(Components)
    security = JsonModel.list(SecurityRequirement)
    tags = JsonModel.list(Tag)
    externalDocs = JsonModel.field(ExternalDocs)
    
    
    