{% for module in meta.modules %}
from .{{meta.module(module).testing_module_name()}} import {{meta.module(module).testing_class_name()}}
{% endfor %}
