from python_dev import pyde
from .model import _model
import click


@pyde.add.command(help='Add all the api models to the development package')
@click.option('--replace/--no-replace', default=False)
@click.option('--echo/--no-echo', default=False)
def api_models(replace, echo):
    _api_models(replace, echo)
    
def _api_models(replace, echo):
    if not pyde.meta.api:
        raise ValueError('You must supply OpenApi data to import all api models')
    for schema in pyde.meta.api.components.schemas:
        _model(schema, replace, echo, False, False)

    






