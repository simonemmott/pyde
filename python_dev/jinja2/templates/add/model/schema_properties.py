{% for name, p in schema.get_all_properties().items() %}
    {{p.name}} = {{p.get_model_method()}}({{p.get_model_type_str()}}{{p.get_model_options()}})
{% endfor %}

