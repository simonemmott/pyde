{% for module in meta.modules %}
from .{{module.testing_module_name()}} import {{module.testing_class_name()}}
{% endfor %}
