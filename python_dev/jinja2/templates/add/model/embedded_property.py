{% for enum in schema.get_enumerations() %}{% include 'add/model/enumeration.py' %}

{% endfor %} 
{% for schema in schema.get_embedded_properties() %}
{% include 'add/model/embedded_property.py' %}

{% endfor %}    
class {{schema.class_name()}}(JsonModel):
{% include 'add/model/schema_properties.py' %}